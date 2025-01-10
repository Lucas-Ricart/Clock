import time
import threading
import msvcrt  # Pour gérer les entrées clavier sur Windows
from datetime import datetime

# Variables globales
heure = None
alarme = None
mode_12h = False
horloge_en_pause = False
dans_menu = False


def afficher_heure():
    """ Affiche l'heure actuelle si le menu n'est pas actif. """
    global heure, dans_menu
    if dans_menu:
        return  # Ne rien afficher si le menu est actif

    heures, minutes, secondes = heure
    if mode_12h:
        periode = "AM" if heures < 12 else "PM"
        heures = heures % 12
        heures = heures if heures != 0 else 12
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
    """ Permet à l'utilisateur de régler l'heure. """
    global heure
    choix = input("\nRéglez l'heure manuellement (m) ou utilisez l'heure actuelle (a) ? (m/a) : ").lower()
    if choix == "m":
        heure_input = input("Entrez l'heure au format hh:mm:ss : ")
        heures, minutes, secondes = map(int, heure_input.split(":"))
        heure = (heures, minutes, secondes)
    elif choix == "a":
        maintenant = datetime.now()
        heure = (maintenant.hour, maintenant.minute, maintenant.second)
        print(f"Heure réglée sur : {heure[0]:02}:{heure[1]:02}:{heure[2]:02}")
    else:
        print("Choix invalide.")


def regler_alarme():
    """ Permet de régler une alarme. """
    global alarme
    try:
        heure_input = input("Réglez l'alarme au format hh:mm:ss : ")
        heures, minutes, secondes = map(int, heure_input.split(":"))
        alarme = (heures, minutes, secondes)
        print(f"Alarme réglée à : {heures:02}:{minutes:02}:{secondes:02}")
    except ValueError:
        print("Format invalide.")


def verifier_alarme():
    """ Vérifie si l'heure actuelle correspond à l'alarme. """
    global alarme, heure
    if alarme and heure == alarme:
        print("\n*** Alarme ! Il est temps ! ***")


def changer_mode_affichage():
    """ Change le mode d'affichage de l'heure. """
    global mode_12h
    choix = input("\nMode 12 heures (1) ou 24 heures (2) : ").strip()
    if choix == "1":
        mode_12h = True
        print("Mode 12 heures activé.")
    elif choix == "2":
        mode_12h = False
        print("Mode 24 heures activé.")
    else:
        print("Choix invalide.")


def afficher_menu():
    """ Gère l'affichage du menu sans bloquer l'horloge. """
    global dans_menu
    dans_menu = True

    while dans_menu:
        print("\n" + "=" * 30)
        print("         MENU PRINCIPAL         ")
        print("=" * 30)
        print("1. Régler une alarme")
        print("2. Régler l'heure")
        print("3. Changer le mode d'affichage")
        print("4. Consulter l'heure actuelle")
        print("5. Quitter le menu")
        print("=" * 30)

        try:
            choix = input("Entrez votre choix (1-5) : ").strip()
            if choix == "1":
                regler_alarme()
            elif choix == "2":
                regler_heure()
            elif choix == "3":
                changer_mode_affichage()
            elif choix == "4":
                heures, minutes, secondes = heure
                print(f"\nHeure actuelle : {heures:02}:{minutes:02}:{secondes:02}")
            elif choix == "5":
                print("\nSortie du menu...")
                dans_menu = False
            else:
                print("\n⚠ Choix invalide. Veuillez entrer un nombre entre 1 et 5.")
        except Exception as e:
            print(f"\nUne erreur s'est produite : {e}. Veuillez réessayer.")


def gestion_pause_et_menu():
    """ Gère la mise en pause et le menu via les touches clavier. """
    global horloge_en_pause, dans_menu
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key.lower() == b'p':  # Pause avec 'p'
                horloge_en_pause = not horloge_en_pause
            elif key == b'\r':  # Entrée pour ouvrir le menu
                afficher_menu()


def loop_horloge():
    """ Thread de gestion de l'affichage de l'horloge. """
    global horloge_en_pause
    while True:
        if not horloge_en_pause:
            incrementer_heure()
            afficher_heure()
            verifier_alarme()
        time.sleep(1)


def main():
    """ Point d'entrée du programme. """
    global heure
    regler_heure()

    # Thread pour l'horloge
    thread_horloge = threading.Thread(target=loop_horloge, daemon=True)
    thread_horloge.start()

    # Thread pour les pauses et le menu
    thread_pause_menu = threading.Thread(target=gestion_pause_et_menu, daemon=True)
    thread_pause_menu.start()

    # Garder le programme actif
    while True:
        time.sleep(1)


if __name__ == "__main__":
    main()
