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
                (labirinto, partenze, destinazioni)=input_file.crea_labirinto_json(self,dictionary)
            return (labirinto, partenze, destinazioni)
        elif estensioneFile == '.tiff':
            (labirinto, partenze, destinazioni)=input_file.leggi_file_tiff(self)
            return (labirinto, partenze, destinazioni)
            

            #print("funzione ancora da implementare")
        else:
            print(" Il formato del file non è supportato")

    def leggi_file_tiff(self):

        # Apri il file TIFF
        with Image.open(self.filepath) as img:
            # Converti l'immagine in una matrice NumPy
            img_array = np.array(img)
            (labirinto, partenze, destinazioni)=input_file.crea_labirinto_tiff(self,img_array)
            return (labirinto, partenze, destinazioni)
    
    def crea_labirinto_json(self,dict):
        """
        metodo che crea il labirito con di costi, direttamente dal un dizionario preso dal file json
        
        sono messe da valore nan

        mancano le posizioni iniziali e quelle finali

        """
        #creo una matrice numpy piena di zeri, con le grandezze del labirinto
        labirinto= np.full((dict['altezza'], dict['larghezza']), 0.)
        partenze=dict['iniziali']
        destinazioni=dict['finale']
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
        return (labirinto, partenze, destinazioni)
    def crea_labirinto_tiff(self,img_array):
        leggenda_colori={'[255 255 255]':0.,'[0 0 0]':np.nan,'[0 255 0]':0.,'[255 0 0]':0.,'[16 16 16]':1.,'[32 32 32]':2.,'[48 48 48]':3.,'[64 64 64]':4.,'[80 80 80]':5.,'[96 96 96]':6.,'[112 112 112]':7.,'[128 128 128]':8.,'[144 144 144]':9.,'[160 160 160]':10.,'[176 176 176]':11.,'[192 192 192]':12.,'[208 208 208]':13.,'[224 224 224]':14.,'[240 240 240]':15.}
        forma_lab=img_array.shape
        partenze=[]
        destinazioni=[]
        labirinto=np.full((forma_lab[0],forma_lab[1]),np.empty)
        for i in range(forma_lab[0]):
            for j in range(forma_lab[1]):
                indice=f'[{img_array[i][j][0]} {img_array[i][j][1]} {img_array[i][j][2]}]'
                labirinto[i,j]=leggenda_colori[indice]
                if indice=='[255 0 0]':
                    coordinate=[]
                    coordinate.append(i)
                    coordinate.append(j)
                    destinazioni.append(coordinate)
                elif indice=='[0 255 0]':
                    coordinate=[]
                    coordinate.append(i)
                    coordinate.append(j)
                    partenze.append(coordinate)    
        return (labirinto, partenze, destinazioni)
    
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
    
    

         
        
        

        
        
