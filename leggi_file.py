# -*- coding: utf-8 -*-

import input_class 
import pandas as pd
import json


def leggi_file_json(self):
    """
    Lettura dei file in formato .json
    """
    try:
        dati_taxi= pd.read_json(self.percorsoFile)
        return dati_taxi
    except:
        print("il file non è in formato json")
   
        
    
    def leggi_immagine():
        """
        Legge un'immagine del labirinto.
        
        L'immagine è un'immagine a colori in formato TIFF, PNG o JPEG che corrisponde a una matrice rettangolare
        un cui i pixel neri corrispondono a posizioni occupate da pareti che non possono essere attraversate, e 
        tutti gli altri pixel corrispondono a posizioni che possono essere attraversate per raggiungere il punto di arrivo.

        I pixel bianchi sono posizioni che non assegnano punti, i pixel grigi indicano caselle che assegnano costi, 
        i pixel verdi indicano le posizioni di partenza, il pixel rosso indica la posizione di arrivo.

        I livelli di grigio possibili sono:

        16 che assegna un costo pari a 1
        32 che assegna un costo pari a 2
        48 che assegna un costo pari a 3
        64 che assegna un costo pari a 4
        80 che assegna un costo pari a 5
        96 che assegna un costo pari a 6
        112 che assegna un costo pari a 7
        128 che assegna un costo pari a 8
        144 che assegna un costo pari a 9
        160 che assegna un costo pari a 10
        176 che assegna un costo pari a 11
        192 che assegna un costo pari a 12
        208 che assegna un costo pari a 13
        124 che assegna un costo pari a 14
        240 che assegna un costo pari a 15

        Returns
        -------
        None.

        """
        return

   
    def get_partenza():
        """
        

        Returns
        -------
        None.

        """
        return
        
    def get_arrivo():
        """
        

        Returns
        -------
        None.

        """
        return

 



  

  