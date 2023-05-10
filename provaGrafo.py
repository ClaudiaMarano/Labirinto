# -*- coding: utf-8 -*-
"""
Created on Fri May  5 14:13:05 2023

@author: diodo
"""

import numpy as np
import heapq

class Nodo:
    def __init__(self, coordinate, costo=float('inf')):
        self.coordinate = coordinate
        self.costo = costo
        self.vicini = []

    def __lt__(self, other):
        return self.costo < other.costo

    def crea_grafo(labirinto, partenze, destinazioni):
        grafo = {}

        # creazione dei nodi del grafo
        for i in range(labirinto.shape[0]):
            for j in range(labirinto.shape[1]):
                if not np.isnan(labirinto[i][j]):
                    coord = (i, j)
                    grafo[coord] = Nodo(coord)

        # creazione degli archi del grafo
        for coord in grafo:
            x, y = coord
            vicini = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            for vicino in vicini:
                if vicino in grafo:
                    grafo[coord].vicini.append(vicino)

        # impostazione dei costi dei nodi di partenza
        for partenza in partenze:
            if partenza in grafo:
                grafo[partenza].costo = 0

        return grafo
    

    def dijkstra(labirinto, grafo, partenza, destinazione):
        coda_priorita = []
        heapq.heappush(coda_priorita, grafo[partenza])
        visitati = set()

        while coda_priorita:
            nodo_attuale = heapq.heappop(coda_priorita)
            if nodo_attuale.coordinate == destinazione:
                break
            if nodo_attuale.coordinate in visitati:
                continue
            visitati.add(nodo_attuale.coordinate)

            for vicino in nodo_attuale.vicini:
                if vicino in visitati:
                    continue
                nuovo_costo = nodo_attuale.costo + 1
                if np.isnan(labirinto[vicino]):
                    nuovo_costo += 1000 # costo elevato per gli ostacoli
                if nuovo_costo < grafo[vicino].costo:
                    grafo[vicino].costo = nuovo_costo
                    heapq.heappush(coda_priorita, grafo[vicino])

        percorso = []
        nodo_attuale = grafo[destinazione]
        
        while nodo_attuale.coordinate != partenza:
            percorso.append(nodo_attuale.coordinate)
            for vicino in nodo_attuale.vicini:
                if grafo[vicino].costo == nodo_attuale.costo - 1:
                    nodo_attuale = grafo[vicino]
                    break
        percorso.append(partenza)
        percorso.reverse()

        return grafo[destinazione].costo, percorso