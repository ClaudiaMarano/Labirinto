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
filepath = './indata/'+str(input('Inserisci il nome del file da leggere con formato tiff o json tra uno di quelli elencati:  '))
#creo un'istanza della classe
inputfile = input_file(filepath)
(labirinto, partenze, destinazioni)= inputfile.leggi_file()
grafo , matrice = input_file.crea_grafo(labirinto)

dataFrame = input_file.trova_tutti_i_cammini(grafo, partenze, destinazioni)
cammini_minimi, peso_cammini_minimi = input_file.cammino_minimo(grafo, partenze, destinazioni)

#costo, path = input_file.dijikstra(grafo, partenze, destinazioni)
#print(path)
for i in range(len(partenze)):
    immagine_rgb = input_file.crea_immagine_rgb(labirinto, partenze[i],destinazioni, cammini_minimi[i])
    print(immagine_rgb.shape)
    percorso_output='./output/'+f'soluzione_ottima{i+1}.jpeg'
    input_file.salva_immagine_jpg(immagine_rgb, percorso_output)

print(labirinto)
print(partenze)  
print(destinazioni)
print(peso_cammini_minimi)
#print(cammini)
#print(cammini_minimi)

    
    



    
    
    
    
    
