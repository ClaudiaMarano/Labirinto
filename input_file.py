# -*- coding: utf-8 -*-
"""
"""

import os
import json
from PIL import Image
import numpy as np

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
        Legge un file in formato Json

        Returns
        -------
        None.

        """
        nome,estensioneFile = os.path.splitext(self.filepath)
        if estensioneFile == '.json':
            with open(self.filepath) as file:
                dictionary = json.load(file)
            return dictionary
        elif estensioneFile == '.tiff':
            return input_file.leggi_file_tiff(self)
            

            #print("funzione ancora da implementare")
        else:
            print(" Il formato del file non è supportato")

    def leggi_file_tiff(self):

        # Apri il file TIFF
        with Image.open(self.filepath) as img:
            # Converti l'immagine in una matrice NumPy
            img_array = np.array(img)
            return img_array
                    
    
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
    
    

         
        
        

        
        
