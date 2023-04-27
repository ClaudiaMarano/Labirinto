# -*- coding: utf-8 -*-
"""
labirinto costituito da una matrice di posizioni, una o più posizioni di partenza e una posizione di arrivo,
e determinare per ogni punto di partenza il percorso che permette di raggiungere il punto di arrivo o, in alternativa, 
se non esiste alcun percorso possibile.

Il labirinto e i punti di partenza e di arrivo possono essere forniti attraverso un file in formato JSON o un'immagine.

"""

class labirinto:
    """
    
    """
    
    def leggi_Json():
        """
        legge un file Json del labirinto.
        
        Il file è un dizionario con le seguenti chiavi:

        "larghezza": un numero che indica il numero di posizioni lungo la dimensione orizzontale;
        "altezza": un numero che indica il numero di posizioni lungo la dimensione verticale;
        "pareti": una lista di segmenti, ogni segmento costituito da un dizionario con chiavi:
        "orientamento": "H" per orizzontale, "V" per verticale;
        "posizione": un coppia di indici che indicano una posizione "iniziale" (per convenzione
        il segmento si estende in orizzontale da sinistra verso destra e in verticale dall'alto verso il basso);
        "lunghezza": un numero che indica il numero di posizioni occupate dal segmento;
        "iniziali": una lista di coppie di indici che indicano ciascuno una posizione di partenza;
        "finale": una coppia di indici che indica la posizione di arrivo;
        "costi": una lista di posizioni con costo, che sono triple costituite da una coppia di indici che indicano una posizione e un valore intero da 1 a 15 che indica il costo.

        Returns
        -------
        None.

        """
    
    
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

