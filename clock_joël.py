import time

while True:
    current_time = time.localtime()   # Récupérer l'heure actuelle

    formatted_time = time.strftime("%H:%M:%S", current_time)    # Format de l'heure hh:mm:ss
    
    # Afficher l'heure
    print(formatted_time, end="\r") 
    
    time.sleep(1) # Attendre une seconde