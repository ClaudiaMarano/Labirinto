# -*- coding: utf-8 -*-
"""
"""

import os
import json


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
        
    
    def leggi_json(self):
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
        else:
            return(" Il file non è in formato json")
        
    
    
    
    

         
        
        

        
        
