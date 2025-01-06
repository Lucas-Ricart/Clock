import time

def regler_heure():
    """
    Permet à l'utilisateur de régler l'heure
    """
    while True:
        try:
            heure_input = input("Entrez l'heure : ")
            heures, minutes, secondes = map(int, heure_input.split(":"))
            if 0 <= heures < 24 and 0 <= minutes < 60 and 0 <= secondes < 60:
                return heures, minutes, secondes
            else:
                print("L'heure, les minutes ou les secondes ne sont pas valides. Essayez à nouveau.")
        except ValueError:
            print("Format invalide. essayez à nouveau.")

def afficher_heure(heure):
    """
    Affiche l'heure 
    """
    heures, minutes, secondes = heure
    print(f"Heure actuelle : {heures:02}:{minutes:02}:{secondes:02}")

def incrementer_heure(heure):
    """
    Incrémente l'heure d'une seconde.
    """
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

def regler_alarme():
    """
    Permet à l'utilisateur de régler une alarme 
    """
    print("Réglage de l'alarme :")
    return regler_heure()

def verifier_alarme(heure_actuelle, alarme):
    """
    Vérifie si l'heure actuelle correspond à l'alarme.
    Affiche un message si l'alarme est déclenchée.
    """
    if heure_actuelle == alarme:
        print("\n*** Alarme ! Il est temps ! ***\n")

def main():
    """
    Fonction principale qui demande à l'utilisateur de régler l'heure et l'incrémente chaque seconde.
    """
    # Demander à l'utilisateur de régler l'heure
    heure = regler_heure()

    # Réglage de l'alarme
    alarme = regler_alarme()

    while True:
        afficher_heure(heure)  # Affiche l'heure actuelle
        verifier_alarme(heure, alarme)  # Vérifie si l'alarme doit sonner
        time.sleep(1)  # Attendre une seconde
        heure = incrementer_heure(heure)  # Incrémenter l'heure

if __name__ == "__main__":
    main()
