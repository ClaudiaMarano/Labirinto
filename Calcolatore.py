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
import heapq

        
    
    


    # def crea_grafo(self, labirinto, partenze, destinazioni): #gli passo labirinto, che è un array di float
    #     """
    #     Crea un dizionario
    #     """
    #     grafo={"grafo":[], "partenze":[], "destinazioni":[]}
        
    #     #salvo i pixel liberi nella chiave "coordinate" del dizionario
    #     #scorro l'altezza della matrice
    #     for i in range(len(labirinto)):
    #         #scorro i singoli pixel in orizzontale partendo dal primo
    #         for j in range(len(labirinto[0])):
    #             if not math.isnan(labirinto[i][j]): #se il valore del pixel non è nan
    #                 nodo=Nodo() #creo un'istanza della classe nodo
    #                 if i>0 and labirinto[i-1][j] != 0:
    #                     grafo["grafo"].append((i-1, j))
    #                 if i<len(labirinto)-1 and labirinto[i+1][j] != 0:
    #                     grafo["grafo"].append((i+1,j))
    #                 if j>0 and labirinto[i][j-1] !=0:
    #                     grafo["grafo"].append((i,j-1))
    #                 if j<len(labirinto[0])-1 and labirinto[i][j+1] !=0:
    #                     grafo["grafo"].append((i,j+1))
                    
    #     return grafo
    
    
    
    # def trova_percorso(grafo, partenze, destinazioni):
    #    """
    #    Returns
    #    -------
    #    None.

    #    """
    #    coda=[(0,partenze)] #creo una tupla
    #    #creo un oggetto di tipo set: collezione di elementi unici e non ordinati
    #    visitati=set()
    #    grafo[partenze].costo=0
       
    #    #trasformo la lista in una coda di priorità: hanno priorità gli elementi più piccoli
    #    while coda:
    #        (costo,nodo) = heapq.heappop(coda)
    #        if nodo in visitati:
    #            continue
    #        visitati.add(nodo) #aggiungo il nodo alla lista dei nodi visitati
    #        if nodo == destinazioni:
    #            break 
           
    #        for nodoAdiacente in grafo[nodo].adiacenti:
    #            nuovo_costo = grafo[nodo].costo+1 #sommo 1 ai costi
    #            if nuovo_costo < grafo[nodoAdiacente].costo:
    #                grafo[nodoAdiacente].costo = nuovo_costo
    #                #inserisce la coppia (costo,nodoAdiacente) nella coda di priorità
    #                heapq.heappush(coda, (nuovo_costo, nodoAdiacente)) 
                   
    #    percorso=[]
    #    nodo_corrente = destinazioni
    #    while nodo_corrente != partenze:
    #        percorso.append(nodo_corrente)
           
    #        #lambda: funzione che restituisce il costo del nodo corrispondente alla chiave x
    #        #nel dizionario grafo (restituisce il valore del campo costo dell'oggetto nodo corrispondente
    #        #alla chiave x nel dizionario del grafo)
           
    #        nodo_corrente = min(grafo[nodo_corrente].adiacenti, key=lambda x: grafo[x].costo)
    #    percorso.append(partenze)
    #    percorso.reverse() #inverte l'ordine degli elementi della lista
       
    #    return percorso, grafo[destinazioni].costo