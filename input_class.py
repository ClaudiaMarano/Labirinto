# -*- coding: utf-8 -*-

import pandas as pd
import json


class input_class:
    
    def gestisci_input(path):
        """
        verifica che il file importato con il path sia .json,
        altrimenti restituisce un messaggio di erroe
        
        Returns
        -------
        None.

        """
        if path.endswith('.json'):
            with open(path, 'r') as f:
                try:
                    json.load(f)
                    print ("Il file è in formato JSON")
                except ValueError:
                    print("Il file non è in formato JSON")
        elif path.endswith('.tiff'):
            print ('il file è in formato .tiff')
        else:
            print ('Formato non riconosciuto')
    
               
        
               
               
                  
  
                 
 
    def leggi_immagine():
         """
         Legge un'immagine del labirinto.
         
         """
    def get_partenza():
        partenza= input ("scegli il punto di partenza")
        return partenza

    def get_arrivo():
        arrivo = input ("scegli il punto di arrivo")
        return arrivo
     
         

    