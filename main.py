# -*- coding: utf-8 -*-
"""
Il programma deve acquisire il layout di un labirinto costituito da una matrice di posizioni, una o più posizioni di partenza 
e una posizione di arrivo, e determinare per ogni punto di partenza il percorso che permette di raggiungere 
il punto di arrivo o, in alternativa, se non esiste alcun percorso possibile.

"""

import os
from input_file import input_file
# from Calcolatore import Nodo

# ottieni i nomi dei file e delle cartelle nella directory
lista_file = os.listdir('./indata/')
print(lista_file)
#fornire il file in input come: indata/nomefile.json
filepath = str(input('Inserisci il nome del file da leggere con formato tiff o json tra uno di quelli elencati:  '))
#creo un'istanza della classe
inputfile = input_file('./indata/'+filepath)
(labirinto, partenze, destinazioni)= inputfile.leggi_file()
grafo , matrice = input_file.crea_grafo(labirinto)


cammini, weight = input_file.trova_tutti_i_cammini(grafo, partenze, destinazioni)
#costo, path = input_file.dijikstra(grafo, partenze, destinazioni)

#grafo , matrice = input_file.crea_grafo(labirinto)


#grafo , matrice = input_file.crea_grafo(labirinto)
#costo, path = input_file.dijikstra(grafo, partenze, destinazioni)
#print(path)


print(labirinto)
print(partenze)  
print(destinazioni)

    
    



    
    
    
    
    
