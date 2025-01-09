import os
import time
import threading
import msvcrt  # Bibliothèque spécifique à Windows pour capter les touches sans bloquer
from datetime import datetime

# Variables globales pour l'heure, l'alarme, le mode d'affichage, et la pause
heure = None
alarme = None
mode_12h = False  # Par défaut, l'affichage est en mode 24 heures
horloge_en_pause = False  # Contrôle si l'horloge est en pause
dans_menu = False  # Contrôle si l'on est dans le menu

def afficher_heure():
    """ Affiche l'heure sur une seule ligne sans retour à la ligne. """
    global heure
    heures, minutes, secondes = heure
    if mode_12h:
        periode = "AM" if heures < 12 else "PM"
        heures = heures % 12
        heures = heures if heures != 0 else 12  # Si heures == 0, il faut afficher 12 en mode 12h
        print(f"\r {heures:02}:{minutes:02}:{secondes:02} {periode}", end="")
    else:
        print(f"\r {heures:02}:{minutes:02}:{secondes:02}", end="")

def incrementer_heure():
    """ Incrémente l'heure d'une seconde. """
    global heure
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
    heure = (heures, minutes, secondes)

def regler_heure():
    """ Permet à l'utilisateur de régler l'heure ou d'utiliser l'heure actuelle. """
    global heure
    while True:
        try:
            choix = input("\nVoulez-vous régler l'heure manuellement (m) ou utiliser l'heure actuelle (a) ? (m/a) : ").lower()
            if choix == "m":
                heure_input = input("Entrez l'heure de départ au format hh:mm:ss : ")
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

def regler_alarme():
    """ Permet à l'utilisateur de régler une alarme. """
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

def mettre_en_pause():
    """ Permet de mettre en pause ou de relancer l'horloge. """
    global horloge_en_pause
    horloge_en_pause = not horloge_en_pause  # Inverse l'état de la pause

def verifier_alarme():
    """ Vérifie si l'heure actuelle correspond à l'alarme. """
    global heure, alarme
    if alarme and heure == alarme:
        print("\n*** Alarme ! Il est temps ! ***")

def afficher_menu():
    """ Affiche le menu principal. """
    global dans_menu
    dans_menu = True  # On est maintenant dans le menu
    print("\nMenu principal :")
    print("1. Régler une nouvelle alarme")
    print("2. Régler l'heure")
    print("3. Changer le mode d'affichage de l'heure")
    print("4. Reprendre l'horloge")

def changer_mode_affichage():
    """ Permet de changer le mode d'affichage de l'heure entre 12 heures et 24 heures. """
    global mode_12h
    choix = input("\nChoisissez le mode d'affichage : 12 heures (1) ou 24 heures (2) : ").strip()
    if choix == "1":
        mode_12h = True
        print("Mode 12 heures activé.")
    elif choix == "2":
        mode_12h = False
        print("Mode 24 heures activé.")
    else:
        print("Choix invalide. Réessayez.")

def menu_principal():
    """ Gère le menu principal. """
    global dans_menu
    while True:
        afficher_menu()
        choix = input("\nEntrez votre choix : ")
        if choix == "1":
            regler_alarme()
        elif choix == "2":
            regler_heure()
        elif choix == "3":
            changer_mode_affichage()
        elif choix == "4":
            dans_menu = False  # Sortir du menu
            break
        else:
            print("Choix invalide. Réessayez.")

def gestion_pause():
    """ Permet de mettre en pause l'horloge en écoutant les entrées clavier de manière non bloquante. """
    global horloge_en_pause
    while True:
        if msvcrt.kbhit():  # Vérifie s'il y a une touche en attente
            key = msvcrt.getch()  # Récupère la touche appuyée
            if key.lower() == b'p':  # Vérifie si la touche 'p' a été pressée
                mettre_en_pause()
            elif key == b'\r':  # Si touche Entrée (pour ouvrir le menu)
                menu_principal()

def main():
    """ Fonction principale qui démarre l'horloge et gère le menu. """
    global heure
    regler_heure()  # Réglage initial de l'heure

    # Lancer un thread pour écouter la touche de pause sans bloquer l'horloge
    thread_pause = threading.Thread(target=gestion_pause, daemon=True)
    thread_pause.start()

    # Affichage et incrémentation de l'heure en continu
    while True:
        if not horloge_en_pause and not dans_menu:  # L'heure défile seulement si on n'est pas dans le menu
            incrementer_heure()
            afficher_heure()
            verifier_alarme()

        # Attendre 1 seconde avant d'actualiser l'heure
        time.sleep(1)

if __name__ == "__main__":
    main()
