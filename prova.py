# -*- coding: utf-8 -*-
"""
"""


import json

class gestisci_input():
    
    def __init__(self):
        self.percorsoFile=('./indata/20-10_marked.json')
    
    
    def leggi_json(self):
        if self.percorsoFile.endswith('.json'):
            with open(self.percorsoFile, 'r') as f:
                try:
                    json.load(f)
                    print ("Il file è in formato JSON")
                except ValueError:
                    print("Il file non è in formato JSON")
        elif self.percorsoFile.endswith('.tiff'):
            print ('il file è in formato .tiff')
        else:
            print ('Formato non riconosciuto')
        
        
    
    
        
    
