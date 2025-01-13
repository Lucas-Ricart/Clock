
import time
from datetime import datetime, timedelta
import os

os.system 
heure = datetime(2025, 1, 9, 9, 27, 50)
heure += timedelta(seconds=1)


while True:
    print(heure.strftime("%H:%M:%S"))
    heure += timedelta(seconds=1)
    time.sleep(1)
    os.system('cls')



import time
from datetime import datetime, timedelta

def afficher_heure(heure_actuelle, alarme=None):
 while True:
        
        print(heure_actuelle.strftime("%H:%M:%S"))
        
        
        if alarme and heure_actuelle == alarme:
            print("Alarme! C'EST L'HEUUUURE!")
        
        
        time.sleep(1)
        
       
        heure_actuelle += timedelta(seconds=1) 


def regler_alarme(heure_alarme): 
    
    alarme = datetime.strptime(heure_alarme, "%H:%M:%S")
    
    
    heure_debut = datetime.strptime("9:28:00", "%H:%M:%S")
    
 
    afficher_heure(heure_debut, alarme)  


if __name__ == "__main__":
    regler_alarme("9:28:00")   










