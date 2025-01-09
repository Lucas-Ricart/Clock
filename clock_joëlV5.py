import os
import time
from datetime import datetime, timedelta
import threading

# Variables globales
heure = None
alarme = None
retour_menu = False

def afficher_heure_en_continu():
    """Affiche l'heure en continu et synchronise avec l'heure réelle."""
    global heure, retour_menu
    while True:
        if not retour_menu:
            os.system('cls' if os.name == 'nt' else 'clear')
            afficher_heure(heure)
            verifier_alarme(heure, alarme)
        heure = incrementer_heure(heure)
        
        # Synchronisation avec l'heure système toutes les minutes
        if heure[1] % 10 == 0 and heure[2] == 0:  # Toutes les 10 minutes
            synchroniser_heure_reelle()
        
        time.sleep(1)

def synchroniser_heure_reelle():
    """Synchronise l'horloge avec l'heure système."""
    global heure
    maintenant = datetime.now()
    heure = (maintenant.hour, maintenant.minute, maintenant.second)

def regler_heure():
    """Permet de régler l'heure manuellement ou d'utiliser l'heure système."""
    global heure
    while True:
        try:
            choix = input("\nVoulez-vous régler l'heure manuellement (m) ou utiliser l'heure actuelle (a) ? (m/a) : ").lower()
            if choix == "m":
                heure_input = input("Entrez l'heure au format hh:mm:ss : ")
                heures, minutes, secondes = map(int, heure_input.split(":"))
                if 0 <= heures < 24 and 0 <= minutes < 60 and 0 <= secondes < 60:
                    heure = (heures, minutes, secondes)
                    return
                else:
                    print("L'heure, les minutes ou les secondes ne sont pas valides. Essayez à nouveau.")
            elif choix == "a":
                maintenant = datetime.now()
                heure = (maintenant.hour, maintenant.minute, maintenant.second)
                print(f"Heure actuelle réglée à : {maintenant.hour:02}:{maintenant.minute:02}:{maintenant.second:02}")
                return
            else:
                print("Choix invalide. Réessayez.")
        except ValueError:
            print("Format invalide. Essayez à nouveau.")

def afficher_heure(heure):
    """Affiche l'heure sur une seule ligne."""
    heures, minutes, secondes = heure
    print(f"\r {heures:02}:{minutes:02}:{secondes:02}", end="")

def incrementer_heure(heure):
    """Incrémente l'heure d'une seconde."""
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
    """Permet à l'utilisateur de régler une alarme."""
    global alarme
    while True:
        try:
            heure_input = input("Réglez l'alarme au format hh:mm:ss : ")
            heures, minutes, secondes = map(int, heure_input.split(":"))
            if 0 <= heures < 24 and 0 <= minutes < 60 and 0 <= secondes < 60:
                alarme = (heures, minutes, secondes)
                print(f"Alarme réglée à : {heures:02}:{minutes:02}:{secondes:02}")
                return
            else:
                print("L'heure, les minutes ou les secondes ne sont pas valides. Essayez à nouveau.")
        except ValueError:
            print("Format invalide. Essayez à nouveau.")

def verifier_alarme(heure_actuelle, alarme):
    """Vérifie si l'heure actuelle correspond à l'alarme."""
    if alarme and heure_actuelle == alarme:
        print("\n*** Alarme ! Il est temps ! ***")

def afficher_menu():
    """Affiche le menu principal."""
    print("\nMenu principal :")
    print("1. Régler une nouvelle alarme")
    print("2. Régler l'heure")
    print("3. Reprendre l'horloge")

def menu_principal():
    """Gère le menu principal."""
    global retour_menu
    retour_menu = True
    while True:
        afficher_menu()
        choix = input("\nEntrez votre choix : ")
        if choix == "1":
            regler_alarme()
        elif choix == "2":
            regler_heure()
        elif choix == "3":
            retour_menu = False
            break
        else:
            print("Choix invalide. Réessayez.")

def main():
    """Fonction principale qui démarre l'horloge."""
    global heure
    regler_heure()
    thread_horloge = threading.Thread(target=afficher_heure_en_continu, daemon=True)
    thread_horloge.start()

    while True:
        input("\nAppuyez sur Entrée pour ouvrir le menu...")
        menu_principal()

if __name__ == "__main__":
    main()
