# -*- coding: utf-8 -*-
"""
"""
import json

class Calcolatore:
    
    """
    determinare per ogni punto di partenza il percorso che permette di raggiungere il punto di arrivo
    o, in alternativa, se non esiste alcun percorso possibile.
    
    Nel caso esista un percorso che permette di raggingere da un punto di partenza il punto di arrivo, 
    oltre al percorso, il programma deve anche fornire il suo costo totale che è la somma dei costi 
    incontrati lungo di esso più la lunghezza del percorso in pixel.
    
    Nel caso esistano più percorsi possibili da un determinato punto di partenza, 
    il programma deve fornire il percorso con il costo minore.
    
    
    Il risultato finale deve essere fornito attraverso:

    un'immagine su cui è indicato il percorso con un colore diverso per ogni punto di partenza;

    un file JSON associato all'immagine con l'informazione del punteggio raggiunto da ogni percorso o, 
    in alternativa, da un messaggio nel caso non esista un percorso possibile da qualcuno delle posizioni di partenza.

    """
    
    def esiste_percorso():
        """
        Boolean:
            True se esiste il percorso
            False se non esiste il percorso

        Returns
        -------
        None.

        """
        
    def lunghezza_percorso():
        """
        

        Returns
        -------
        None.

        """
    def costo_percorso():
        """
        
        Returns
        -------
        None.

        """
    def percorso_costo_minore():
        """
        

        Returns
        -------
        None.

        """
        
    def lunghezza_pixel():
        """
    

        Returns
        -------
        None.

        """
    def leggi_json(path):
        """
        
        Returns
        -------
        None.

        """
    with open (path, 'r') as f:
        data=json.load(f)

