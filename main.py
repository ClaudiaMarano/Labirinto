# -*- coding: utf-8 -*-
"""
Il programma deve acquisire il layout di un labirinto costituito da una matrice di posizioni, una o più posizioni di partenza 
e una posizione di arrivo, e determinare per ogni punto di partenza il percorso che permette di raggiungere 
il punto di arrivo o, in alternativa, se non esiste alcun percorso possibile.

"""

from input_file import input_file

#fornire il file in input come: indata/nomefile.json
filepath = input('Inserisci il nome del file da leggere compreso il formato del file:  ')

#creo un'istanza della classe
inputfile = input_file('./indata/'+filepath)
(labirinto, partenze, destinazioni)= inputfile.leggi_file()
#print(dict)

print(labirinto)
print(partenze)
print(destinazioni)

    
    



    
    
    
    
    
