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
from input_file import input_file

class Calcolatore:
    

# =============================================================================
#     def cammini(partenze, destinazioni, valid_positions):
#         
#         partenze=[tuple(sublist) for sublist in partenze]
#         partenze=tuple(partenze)
#         destinazioni=[tuple(sublist) for sublist in destinazioni]
#         destinazioni=tuple(destinazioni)
#         # Creiamo una coda vuota per tener traccia dei percorsi
#         queue = []
#         # Iniziamo l'algoritmo con il primo nodo, con un peso pari a 0
#         # e inizializziamo il percorso inserendo al suo interno solo il primo nodo
#         for partenza in partenze:
#             for destinazione in destinazioni:
#                 heapq.heappush(queue, (0, partenza, [partenza]))
#                 # Creiamo un dizionario per tenere traccia dei nodi visitati con il loro peso minimo
#                 visited = {partenza: 0}
#                 # Creiamo una variabile per tener traccia del peso totale del percorso
#                 weight_tot = 0
#                 # Fintanto che ci sono nodi nella coda
#                 while queue:
#                     # Prendiamo l'elemento a peso minimo dalla coda e lo assegniamo alle variabili curr_weight, curr_pos e path
#                     curr_weight, curr_pos, path = heapq.heappop(queue)
#                     # Se il nodo corrente è quello finale
#                     if curr_pos == destinazione:
#                         weight_tot = curr_weight
#                         return path, weight_tot
#                         
#                     # Altrimenti, per ogni posizione adiacente al nodo corrente si verifica se esse siano state già visitate
#                     for next_pos, weight in valid_positions:
#                         # Se la posizione adiacente non è stata visitata
#                         if next_pos not in visited:
#                             # Calcoliamo il nuovo peso totale
#                             new_weight = curr_weight + weight
#                             # Aggiungiamo la posizione adiacente al dizionario dei nodi visitati
#                             visited[next_pos] = new_weight
#                             # Creiamo una nuova lista del percorso con la posizione adiacente
#                             new_path = list(path)
#                             new_path.append(next_pos)
#                             # Inseriamo la posizione adiacente con il nuovo peso totale e il nuovo percorso nella coda
#                             heapq.heappush(queue, (new_weight, next_pos, new_path))
#                   # Se non ci sono percorsi validi, ritorna un valore nullo (None)
#         return new_weight, new_path
# 
#     
# =============================================================================
    
    def Risolutore_labirinto():
        """
        Funzione che implementa i passaggi necessari alla risoluzione del labirinto,
        implementando i metodi creati
        
        """
        
        #carico il labirinto in base al tipo di formato
          #json
          #tiff
        
        #chiamo la funzione per trovare tutti i cammini
        
        #chiamo la funzione per trovare il cammino minimo
        
        #restituito un output 
        
        
        
        pass


        
    
   