# -*- coding: utf-8 -*-
"""
"""

import os
import json
from PIL import Image
import numpy as np
import networkx as nx
import heapq
import matplotlib as plt
import pandas as pd
import math


class input_file:
   
    """
    Classe che implementa e gestisce l'input
    
    Riceve in ingresso il file
    Deve gestire che tipo di file sia (.json o .tiff)
    Chiede in input il punto di partenza 
    Chiede in input il punto di arrivo
    
    """
    

    def __init__(self, filepath):
        
        self.filepath = filepath
        
        
        
    
    def leggi_file(self):
        """
        input: self.filepath della classe

        Riconosce se il file nella path è un in formato json o tiff, altrimenti non lo legge.
        A seconda del tipo di file richiama il metedo adeguato per la creazione della matrice labirinto, della lista delle partenze e
        della lista delle destinazioni.

        output: matrice del labirinto, lista partenze e lista destinazioni.
        -------
        None.

        """
    
        try:
            percorso,estensioneFile = os.path.splitext(self.filepath)
            percorsolist=percorso.split('/')
            nome=percorsolist[2]
            nomefile=nome+estensioneFile
            lista_file = os.listdir('./indata/')
            if nomefile in lista_file:
                if estensioneFile == '.json':
                    with open(self.filepath) as file:
                        dictionary = json.load(file)
                        (labirinto, partenze, destinazioni)=input_file.crea_labirinto_json(self,dictionary)
                        return (labirinto, partenze, destinazioni)
                elif estensioneFile == '.tiff':
                    (labirinto, partenze, destinazioni)=input_file.leggi_file_tiff(self)
                    return (labirinto, partenze, destinazioni)                   

                        #print("funzione ancora da implementare")
            else:
                lista_file = os.listdir('./indata/')
                print(lista_file)
                self.filepath='./indata/'+str(input('il file cercato non è presente nella cartella. Prova con un altro nome: '))
                return input_file.leggi_file(self)

        except TypeError:
            lista_file = os.listdir('./indata/')
            print(lista_file)
            self.filepath='./indata/'+str(input('il file cercato non è presente nella cartella. Prova con un altro nome: '))
            return input_file.leggi_file(self)
    
    
    
    def leggi_file_tiff(self):
        """
        input:self.path della classe

        legge l'immagine e la converte in una matrice a tre dimensioni dove le prime due grandezze sono le lunghezze
        del labirinto e la terza è tre corrispondente ai tre colori RGB.
        la mtrice viene richiamta da un altro metodo che restuisce una mtrice labirinto, una lista di posizioni di partenza e una lista di destinazioni.

        output: matrice labirinto, partenze e destinazioni.
        """

        # Apri il file TIFF
        with Image.open(self.filepath) as img:
            # Converti l'immagine in una matrice NumPy
            img_array = np.array(img)
            (labirinto, partenze, destinazioni)=input_file.crea_labirinto_tiff(self,img_array)
            return (labirinto, partenze, destinazioni)
        
        
    
    def crea_labirinto_json(self,dict):
        """
        inpunt: dizionario con caratteristiche del labirinto

        metodo che crea il labirito sostituendo nelle coordinate specificate nel dizionario i costi corrispondenti 
        e pone al posto delle pareti il valore nan.
        inoltre salva in una lista di liste le posizioni di partenza e di destinazione.

        output: matrice labirinto, lista delle posizioni di partenza e lista delle posizioni di destinazione
        """
        #creo una matrice numpy piena di zeri, con le grandezze del labirinto
        labirinto= np.full((dict['altezza'], dict['larghezza']), 1.)
        partenze=dict['iniziali']
        destinazioni=dict['finale']
        #creo le pareti sostiuendo gli zeri con nan
        for i in range(len(dict['pareti'])):
            if dict['pareti'][i]['orientamento']=='H':
                indice1=int(dict['pareti'][i]['posizione'][0])
                indice2=int(dict['pareti'][i]['posizione'][1])
                indice3=int(dict['pareti'][i]['posizione'][1])+int(dict['pareti'][i]['lunghezza'])
                labirinto[indice1,indice2:indice3]=np.nan
            else:
                indice1=int(dict['pareti'][i]['posizione'][0])
                indice2=int(dict['pareti'][i]['posizione'][0])+int(dict['pareti'][i]['lunghezza'])
                indice3=int(dict['pareti'][i]['posizione'][1])
                labirinto[indice1:indice2,indice3]=np.nan
        #sostuisco con il costo le posizioni specificate
        for i in range(len(dict['costi'])):
            posizione_orizzontale=dict['costi'][i][0]
            posizione_verticale=dict['costi'][i][1]
            labirinto[posizione_orizzontale,posizione_verticale]=float(dict['costi'][i][2])
        return (labirinto, partenze, destinazioni)
    
    
    
    def crea_labirinto_tiff(self,img_array):
        """
        inpunt: matrice a tre dimensioni aveente per ogni pixel la sua corrispondente triade RGB

        metodo che crea il labirito sostituendo nelle coordinate specificate del dizionario i costi corrispondenti 
        e pone al posto delle pareti il valore nan.
        inoltre salva in una lista di liste le posizioni di partenza e di destinazione.

        output: matrice labirinto, lista delle posizioni di partenza e lista delle posizioni di destinazione
        """
        leggenda_colori={'[255 255 255]':1.,'[0 0 0]':np.nan,'[0 255 0]':0.,'[255 0 0]':0.,'[16 16 16]':1.,'[32 32 32]':2.,'[48 48 48]':3.,'[64 64 64]':4.,'[80 80 80]':5.,'[96 96 96]':6.,'[112 112 112]':7.,'[128 128 128]':8.,'[144 144 144]':9.,'[160 160 160]':10.,'[176 176 176]':11.,'[192 192 192]':12.,'[208 208 208]':13.,'[224 224 224]':14.,'[240 240 240]':15.}
        forma_lab=img_array.shape
        partenze=[]
        destinazioni=[]
        labirinto=np.full((forma_lab[0],forma_lab[1]),np.empty)
        for i in range(forma_lab[0]):
            for j in range(forma_lab[1]):
                indice=f'[{img_array[i][j][0]} {img_array[i][j][1]} {img_array[i][j][2]}]'
                labirinto[i,j]=leggenda_colori[indice]
                if indice=='[255 0 0]':
                    coordinate=[]
                    coordinate.append(i)
                    coordinate.append(j)
                    destinazioni.append(coordinate)
                elif indice=='[0 255 0]':
                    coordinate=[]
                    coordinate.append(i)
                    coordinate.append(j)
                    partenze.append(coordinate)
        
        return (labirinto, partenze, destinazioni)
    
    

    def crea_nodi(labirinto):
        G = nx.Graph()
        for i, row in enumerate(labirinto):
            for j, val in enumerate(row):
                if not np.isnan(val):
                    G.add_node((i, j), weight=1)
    
    

    
    def crea_grafo(labirinto):
        #creo un'istanza del grafo
        G = nx.Graph()
        righe,colonne=labirinto.shape
        for i, row in (enumerate(labirinto)): #i tiene traccia della riga, row contiene la riga
            for j, val in enumerate(row): #j tiene conto della colonna, val del valore della cella
                if not np.isnan(val): #se l'elemento della cella non è nan 
                #controlla se la cella corrente ha una cella adiacente sopra di essa, 
                #e se quella cella adiacente non è un valore mancante.
                    if i > 0 and not np.isnan(labirinto[i-1, j]):
                        G.add_edge((i, j), (i-1, j), weight= labirinto[i-1,j]) #aggiungo arco
                    if j > 0 and not np.isnan(labirinto[i, j-1]):
                        G.add_edge((i, j), (i,j-1), weight = labirinto[1,j-1])
                    # Riguarda le ultime caselle
                    if i < righe-1 and not np.isnan(labirinto[i+1, j]):
                        G.add_edge((i, j), (i+1, j), weight=val)
                    if j < colonne-1 and not np.isnan(labirinto[i, j+1]):
                        G.add_edge((i, j), (i, j+1), weight= val)
        adj_matrix = nx.to_numpy_array(G)
        return G, adj_matrix
    
                        

 
# =============================================================================
#     def posizioni_adiacenti(labirinto,curr_pos):
#         
#         """
#         Questa funzione verifica quali tra le 4 posizioni adiacenti alla posizione corrente
#         siano uno spazio percorribile e non un muro.
#         Parameters
#         ----------
#         pos : tuple
#             Rappresenta la casella di cui valutare le adiacenti.
# 
#         Returns
#         -------
#         valid_positions : list
#             Restituisce tutte le caselle in cui è possibile spostarsi.
#         """
#         
#         x, y = curr_pos
#         adjacent_positions = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
#         valid_positions = []
#         for i,j in adjacent_positions:
#             if i >= 0 and j >= 0 and i<len(labirinto) and j<len(labirinto[0]) and not math.isnan(labirinto[i][j]):
#                 valid_positions.append(((i,j), labirinto[i][j]))
#         return valid_positions
# =============================================================================
    
    

    def trova_tutti_i_cammini(grafo, partenze, destinazioni):
        
        # Trasforma ogni sottolista in una tupla
        partenze=[tuple(sublist) for sublist in partenze]
        partenze=tuple(partenze)
        destinazioni=[tuple(sublist) for sublist in destinazioni]
        destinazioni=tuple(destinazioni)
        
        #Calcolo tutti i possibili cammini fra partenza/e e destinazione/i
        cammini = []
        peso_cammini=[]
        lunghezza_cammino=0
        for partenza in partenze:
            for destinazione in destinazioni:
                if grafo.has_node(partenza) and grafo.has_node(destinazione):
                    if nx.has_path(grafo,partenza,destinazione):
                        for cammino in nx.all_simple_paths(grafo, source=partenza, target=destinazione):
                            pd.Series(cammino)
                            for u, v, attrs in grafo.edges(data=True):
                                peso_arco= attrs['weight']
                            
                            cammini.append(cammino)
                            lunghezza_cammino=len(cammino)
                            # Itera su tutti gli archi del grafo
                            for u, v, attrs in grafo.edges(data=True):
                                peso_arco= attrs['weight']  # Accedi al peso dell'arco
                                peso_totale=peso_arco+lunghezza_cammino
                                peso_cammini.append(peso_totale)
                            
        #creo un dataFrame con i risultati di tutti i cammini
        serie_cammini = pd.Series(cammini)
        serie_pesi = pd.Series(peso_cammini)
        dataframe = pd.DataFrame({'Cammini': serie_cammini, 'Pesi': serie_pesi})
        return  dataframe


    def get_pesi(grafo, cammini):
        for cammino in cammini:
            for nodo in cammino:
                source=nodo[nodo]
                target=nodo[nodo+1]
                edge_data = grafo.get_edge_data(source, target)
                weight = edge_data['weight']
                print(f"Nodo: {target}, Peso: {weight}")

    def cammino_minimo(grafo, partenze, destinazioni):
        
        # Trasforma ogni sottolista in una tupla
        partenze=[tuple(sublist) for sublist in partenze]
        partenze=tuple(partenze)
        destinazioni=[tuple(sublist) for sublist in destinazioni]
        destinazioni=tuple(destinazioni)
        
        # converti in insiemi di nodi
        partenze_set = set(partenze)
        destinazioni_set = set(destinazioni)
        cammini_minimi = [] #calcola i cammini minimi fra partenza/e e destinazione/i
        peso_cammini_minimi=[]
        # scorri tutte le coppie di partenza e destinazione
        for nodo_p in partenze_set:
            for nodo_d in destinazioni_set:
                # verifico che i nodi di partenza e destinazione siano nel grafo
                if grafo.has_node(nodo_p) and grafo.has_node(nodo_d):
                    if nx.has_path(grafo,nodo_p,nodo_d):
                        #Returns the shortest weighted path from source to target in G.
                        cammino_minimo = nx.dijkstra_path(grafo, nodo_p, nodo_d)
                        cammini_minimi.append(cammino_minimo)
                            
                        #Returns the shortest weighted path length in G from source to target
                        peso_cammino=nx.dijkstra_path_length(grafo, nodo_p, nodo_d)
                        peso_cammini_minimi.append(peso_cammino)
                        
                        
        return cammini_minimi, peso_cammini_minimi
    
    
    
        
    def lunghezza_percorso_in_pixel(dataFrame):
        """
        Se ho trovato un percorso che collega partenza e destinazione, 
        questa funzione calcola la lunghezza in pixel fra i due punti specificati. 
        
        Riceve in ingresso il path dei cammini trovati
        
        Per calcolare la lunghezza in pixel, calcoliamo la distanza euclidea fra le celle

        Returns
        -------
        None.

        """
        lunghezze=[]
        lunghezza=0
        #considero paths come una lista di tuple che contengono le posizioni occupate dai nodi in sequenza
        for path in dataFrame['Cammini'].to_list():
            for i in range(len(path) - 1):
                x1, y1 = path[i]
                x2, y2 = path[i + 1]
                distanza = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
                lunghezza += distanza
            lunghezze.append(lunghezza)
        return lunghezze
    
    
    
        
    def plot_grafo(G):
        pos = nx.spring_layout(G) # posizionamento dei nodi
        nx.draw_networkx_nodes(G, pos, node_color='lightblue') # disegna i nodi
        nx.draw_networkx_edges(G, pos, edge_color='grey') # disegna gli archi
        nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif') # disegna le etichette dei nodi
        # mostra il grafo
        plt.axis('off') # rimuove gli assi
        plt.show()
    



    def crea_immagine_rgb(labirinto, partenze, destinazioni, cammini_minimi):
        altezza, larghezza = labirinto.shape
        immagine_rgb = np.zeros((altezza, larghezza, 3), dtype=np.uint8)
        
        for i in range(altezza):
            for j in range(larghezza):
                valore = labirinto[i, j]
                if np.isnan(valore):
                    immagine_rgb[i, j] = (0,0,0)
                else:
                    immagine_rgb[i, j] = (255,255,255)
        for i in range(len(cammini_minimi)):
            immagine_rgb[cammini_minimi[i][0]][cammini_minimi[i][1]]=(138, 43, 226)
        immagine_rgb[partenze[0]][partenze[1]]=(0,255,0)
        immagine_rgb[destinazioni[0][0]][destinazioni[0][1]]=(255,0,0)
        return immagine_rgb




    def salva_immagine_jpg(immagine_rgb, percorso_immagine):
        dimensioni= immagine_rgb.shape
        altezza=dimensioni[0]
        larghezza =dimensioni[1]
        immagine = Image.fromarray(immagine_rgb)
        area_visualizzazione=(0,0,larghezza,altezza)
        immagine_cropped = immagine.crop(area_visualizzazione)
        immagine_cropped.save(percorso_immagine, "JPEG")




        
        
        
        
        








    # def dijikstra(grafo, partenze, destinazioni):
    #     """
    #     Prende in input il grafo G, il nodo di partenza start e il nodo di arrivo end.
    #     Utilizza una coda di priorità (implementata come un heap binario) per esplorare i
    #     nodi del grafo in ordine di costo crescente. Ad ogni iterazione, estrae il nodo
    #     con il costo più basso dalla coda di priorità e aggiunge i suoi vicini alla coda
    #     di priorità con il costo aggiornato.

    #     Returns
    #     -------
    #     None.

    #     """
    #     partenze=tuple(partenze[0])
    #     destinazioni=tuple(destinazioni[0])
    #     #Creo una coda di priorità: inserisco i nodi in ordine crescente di peso
    #     heap = [partenze]
    #     visited = [] #definisco un insieme vuoto dei nodi visitati
    #     cost = 0
        
    #     #continua finchè la coda di priorità non è vuota
    #     while heap:
    #         # Estrai il nodo con la priorità più bassa
    #         lowNode = heapq.heappop(heap) #nodo con priorità piu bassa
    #         nodoConsiderato=lowNode
    #         path = [nodoConsiderato]
    #         #nodoConsiderato = lowNode #estrae il nodo corrente dal percorso estratto.
            
    #         #verfico se il nodo estratto dalla coda è la destinazione;
    #         #se lo è, restituisce il percorso e il costo
    #         if nodoConsiderato == destinazioni:
    #             cost=1
    #             path=[nodoConsiderato]
            
    #         elif nodoConsiderato not in visited: #se il nodo non è stato visitato
    #             visited.append(nodoConsiderato)
    #             vicini = list(nx.neighbors(grafo,nodoConsiderato))
    #             for neighbor in vicini: #per ogni vicino del nodo considerato
    #                 weight = grafo[nodoConsiderato][neighbor]['weight']
    #                 cost = cost + weight
    #                 path = list(path)
    #                 path.append(neighbor)
    #                 heapq.heappush(heap, (cost, path))  #Controlla questa rig
                
    #         return cost, path
            
       
            
        
        
    
    
    
    
        
