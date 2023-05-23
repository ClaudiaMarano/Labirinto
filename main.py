# -*- coding: utf-8 -*-
"""
Il programma deve acquisire il layout di un labirinto costituito da una matrice di posizioni, una o più posizioni di partenza 
e una posizione di arrivo, e determinare per ogni punto di partenza il percorso che permette di raggiungere 
il punto di arrivo o, in alternativa, se non esiste alcun percorso possibile.

"""

import os
from input_file import input_file
from Calcolatore import Calcolatore
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



# for nodo in grafo.nodes:
#     posizioni_adiacenti_valide=input_file.posizioni_adiacenti(labirinto, nodo)
    
# weight, path = Calcolatore.cammini(partenze, destinazioni, posizioni_adiacenti_valide)   


dataFrame = input_file.trova_tutti_i_cammini(grafo, partenze, destinazioni)
#grafo2, matrice2=input_file(labirinto)
#lunghezza=input_file.lunghezza_percorso_in_pixel(dataFrame)
cammini_minimi, peso_cammini_minimi = input_file.cammino_minimo(grafo, partenze, destinazioni)
#posizioni = input_file.get_adjacent_positions(grafo, partenze)

#path_tot, wieght_tot=input_file(grafo,partenze,destinazioni)

#print(path)
cartella = './output'  # Specifica il percorso alla cartella desiderata
# Ottenere l'elenco dei file nella cartella
elenco_file = os.listdir(cartella)
# Rimuovere ogni file nella cartella
print(len(partenze))
print(len(cammini_minimi))
for file in elenco_file:
    percorso_file = os.path.join(cartella, file)  # Crea il percorso completo al file
    os.remove(percorso_file)
for i in range(len(partenze)):
    print(i)
    immagine_rgb = input_file.crea_immagine_rgb(labirinto, partenze[i],destinazioni, cammini_minimi[i])
    percorso_output='./output/'+f'soluzione_ottima{i+1}.jpeg'
    input_file.salva_immagine_jpg(immagine_rgb, percorso_output)

# print(labirinto)
# print(partenze)  
# print(destinazioni)
# print(peso_cammini_minimi)
# #print(cammini)
#print(cammini_minimi)

    
    



    
    
    
    
    
