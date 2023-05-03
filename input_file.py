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
    
    def crea_labirinto_json(self,dict):
        """
        metodo che crea il labirito con di costi, direttamente dal un dizionario preso dal file json
        
        sono messe da valore nan

        mancano le posizioni iniziali e quelle finali

        restistituisce una matrice numpy
        """
        #creo una matrice numpy piena di zeri, con le grandezze del labirinto
        labirinto= np.full((dict['altezza'], dict['larghezza']), float(0))
        #creo le pareti sostiuendo gli zeri con nan
        for i in range(len(dict['pareti'])):
            if dict['pareti'][i]['orientamento']=='H':
                indice1=int(dict['pareti'][i]['posizione'][0])
                indice2=int(dict['pareti'][i]['posizione'][1])
                indice3=int(dict['pareti'][i]['posizione'][1])+int(dict['pareti'][i]['lunghezza'])
                labirinto[indice1,indice2:indice3]=np.nan
            else:
                indice1=int(dict['pareti'][i]['posizione'][0])
                indice2=int(dict['pareti'][i]['posizione'][0])+int(dict['pareti'][i]['lunghezza'])
                indice3=int(dict['pareti'][i]['posizione'][1])
                labirinto[indice1:indice2,indice3]=np.nan
        #sostuisco con il costo le posizioni specificate
        for i in range(len(dict['costi'])):
            posizione_orizzontale=dict['costi'][i][0]
            posizione_verticale=dict['costi'][i][1]
            labirinto[posizione_orizzontale,posizione_verticale]=float(dict['costi'][i][2])
        return labirinto
    
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
    
    

         
        
        

        
        
