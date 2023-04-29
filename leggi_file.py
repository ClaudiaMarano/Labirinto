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
   
        
    
    

  

  