import os
import time
from datetime import datetime
import threading

# Variables globales pour l'heure et l'alarme
heure = None
alarme = None
retour_menu = False  # Contrôle si on est dans le menu ou non


def afficher_heure_en_continu():
    """ Fonction exécutée dans un thread pour afficher l'heure en continu """
    global heure, retour_menu
    while True:
        if not retour_menu:  # L'heure ne s'affiche pas pendant qu'on est dans le menu
            os.system('cls' if os.name == 'nt' else 'clear')  # Efface l'écran
            afficher_heure(heure)
            verifier_alarme(heure, alarme)
        heure = incrementer_heure(heure)
        time.sleep(1)


def regler_heure():
    """ Permet à l'utilisateur de régler l'heure ou d'utiliser l'heure actuelle.  """
    global heure
    while True:
        try:
            choix = input("\nVoulez-vous régler l'heure manuellement (m) ou utiliser l'heure actuelle (a) ? (m/a) : ").lower()
            if choix == "m":
                heure_input = input("Entrez l'heure de départ  : ")
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
    """ Affiche l'heure au format hh:mm:ss sur une seule ligne.  """
    heures, minutes, secondes = heure
    print(f"\rHeure actuelle : {heures:02}:{minutes:02}:{secondes:02}", end="")


def incrementer_heure(heure):
    """Incrémente l'heure d'une seconde.    """
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
    Permet à l'utilisateur de régler une alarme.
    """
    global alarme
    while True:
        try:
            heure_input = input("Réglez l'alarme au format  : ")
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
    """
    Vérifie si l'heure actuelle correspond à l'alarme.
    Affiche un message si l'alarme est déclenchée.
    """
    if alarme and heure_actuelle == alarme:
        print("\n*** Alarme ! Il est temps ! ***")


def afficher_menu():
    """
    Affiche le menu principal.
    """
    print("\nMenu principal :")
    print("1. Régler une nouvelle alarme")
    print("2. Régler l'heure")
    print("3. Reprendre l'horloge")


def menu_principal():
    """
    Gère le menu principal.
    """
    global retour_menu
    retour_menu = True  # Indique qu'on est dans le menu
    while True:
        afficher_menu()
        choix = input("\nEntrez votre choix : ")
        if choix == "1":
            regler_alarme()
        elif choix == "2":
            regler_heure()
        elif choix == "3":
            retour_menu = False  # Sortie du menu
            break
        else:
            print("Choix invalide. Réessayez.")


def main():
    """
    Fonction principale qui démarre l'horloge et gère le menu.
    """
    global heure
    regler_heure()  # Réglage initial de l'heure

    # Lancer le thread pour afficher l'heure en continu
    thread_horloge = threading.Thread(target=afficher_heure_en_continu, daemon=True)
    thread_horloge.start()

    while True:
        input("\nAppuyez sur Entrée pour ouvrir le menu...")
        menu_principal()


if __name__ == "__main__":
    main()
