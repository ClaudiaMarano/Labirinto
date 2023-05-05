# -*- coding: utf-8 -*-
"""
determinare per ogni punto di partenza il percorso che permette di raggiungere il punto di arrivo
o, in alternativa, se non esiste alcun percorso possibile.

Nel caso esista un percorso che permette di raggingere da un punto di partenza il punto di arrivo, 
oltre al percorso, il programma deve anche fornire il suo costo totale che è la somma dei costi 
incontrati lungo di esso più la lunghezza del percorso in pixel.

Se esistano più percorsi possibili da un determinato punto di partenza, 
il programma deve fornire il percorso con il costo minore.

"""
import math

class Nodo: #consideriamo i pixel come nodi
    #Consideriamo la matrice del labirinto come un grafo
    
    def __init__(self):
        self.costo = float('inf')
        self.adiacenti = []   #lista di nodi adiacenti
    
    def crea_grafo(self, labirinto): #gli passo labirinto, che è un array di float
        grafo={}
        #scorro l'altezza della matrice
        for i in range(len(labirinto)):
            #scorro i singoli pixel in orizzontale partendo dal primo
            for j in range(len(labirinto[0])):
                if not math.isnan(labirinto[i][j]): #se il valore del pixel non è nan
                    nodo=Nodo() #creo un'istanza della classe nodo
                    if i>0 and labirinto[i-1][j] != 0:
                        nodo.adiacenti.append((i-1, j))
                    if i<len(labirinto)-1 and labirinto[i+1][j] != 0:
                        nodo.adiacenti.append((i+1,j))
                    if j>0 and labirinto[i][j-1] !=0:
                        nodo.adiacenti.append((i,j-1))
                    if j<len(labirinto[0])-1 and labirinto[i][j+1] !=0:
                        nodo.adiacenti.append((i,j+1))
                    grafo[(i,j)]=nodo
        return grafo
                

    
    
