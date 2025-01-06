import time

def regler_heure():
    """
    Permet à l'utilisateur de régler l'heure.
    """
    while True:
        try:
            heure_input = input("Entrez l'heure : ")
            heures, minutes, secondes = map(int, heure_input.split(":"))
            if 0 <= heures < 24 and 0 <= minutes < 60 and 0 <= secondes < 60:
                return heures, minutes, secondes
            else:
                print("L'heure. Essayez à nouveau.")
        except ValueError:
            print("Format invalide.  essayez à nouveau.")

def afficher_heure(heure):
    """ Affiche l'heure   """
    heures, minutes, secondes = heure
    print(f"Heure actuelle : {heures:02}:{minutes:02}:{secondes:02}")

def incrementer_heure(heure):
  
    heures, minutes, secondes = heure
    secondes += 1
    if secondes == 60:
        secondes = 0
        minutes += 1
        if minutes == 60:
            minutes = 0
            heures += 1
            if heures == 24:
                heures = 0
    return heures, minutes, secondes

def main():
   
    # Demander à l'utilisateur de régler l'heure
    heure = regler_heure()

    while True:
        afficher_heure(heure)  # Affiche l'heure actuelle
        time.sleep(1)  # Attendre une seconde
        heure = incrementer_heure(heure)  

if __name__ == "__main__":
    main()
