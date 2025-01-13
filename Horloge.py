import customtkinter as ctk
from tkinter import messagebox, simpledialog
import time
import threading
from datetime import datetime
import pygame  # Bibliothèque pour jouer des sons

# Initialiser pygame pour gérer les sons
pygame.mixer.init()

# Variables globales pour l'heure, l'alarme, et la pause
heure = None
alarme = None
mode_12h = False
horloge_en_pause = False

# Charger le son de l'alarme (remplacez ce chemin par le vôtre)
son_alarme = pygame.mixer.Sound("Reveille.mp3")

# Configurer CustomTkinter
ctk.set_appearance_mode("dark")  # Modes : "dark", "light", "system"
ctk.set_default_color_theme("blue")  # Thèmes : "blue", "green", "dark-blue"


def afficher_heure():
    """ Affiche l'heure sur l'interface graphique """
    global heure
    heures, minutes, secondes = heure
    if mode_12h:
        periode = "AM" if heures < 12 else "PM"
        heures = heures % 12
        heures = heures if heures != 0 else 12  # Si heures == 0, il faut afficher 12 en mode 12h
        time_str = f"{heures:02}:{minutes:02}:{secondes:02} {periode}"
    else:
        time_str = f"{heures:02}:{minutes:02}:{secondes:02}"
    label_heure.configure(text=time_str)


def incrementer_heure():
    """ Incrémente l'heure d'une seconde """
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
    """ Permet à l'utilisateur de régler l'heure (manuellement ou automatiquement) """
    global heure
    choix = ctk.CTkInputDialog(text="Voulez-vous régler l'heure manuellement (m) ou automatiquement (a) ?", title="Réglage de l'heure").get_input()
    if choix and choix.lower() == "m":
        heure_input = ctk.CTkInputDialog(text="Entrez l'heure au format hh:mm:ss :", title="Réglage de l'heure").get_input()
        try:
            heures, minutes, secondes = map(int, heure_input.split(":"))
            if 0 <= heures < 24 and 0 <= minutes < 60 and 0 <= secondes < 60:
                heure = (heures, minutes, secondes)
                afficher_heure()
            else:
                messagebox.showerror("Erreur", "L'heure, les minutes ou les secondes sont invalides.")
        except ValueError:
            messagebox.showerror("Erreur", "Format d'heure invalide.")
    elif choix and choix.lower() == "a":
        maintenant = datetime.now()
        heure = (maintenant.hour, maintenant.minute, maintenant.second)
        afficher_heure()
    else:
        messagebox.showerror("Erreur", "Choix invalide.")


def regler_alarme():
    """ Permet à l'utilisateur de régler une alarme """
    global alarme
    heure_input = ctk.CTkInputDialog(text="Entrez l'alarme au format hh:mm:ss :", title="Réglage de l'alarme").get_input()
    try:
        heures, minutes, secondes = map(int, heure_input.split(":"))
        if 0 <= heures < 24 and 0 <= minutes < 60 and 0 <= secondes < 60:
            alarme = (heures, minutes, secondes)
            messagebox.showinfo("Alarme réglée", f"Alarme réglée à {heures:02}:{minutes:02}:{secondes:02}")
        else:
            messagebox.showerror("Erreur", "L'heure entrée est invalide.")
    except ValueError:
        messagebox.showerror("Erreur", "Format d'heure invalide.")


def mettre_en_pause():
    """ Permet de mettre en pause ou de relancer l'horloge """
    global horloge_en_pause
    horloge_en_pause = not horloge_en_pause
    if horloge_en_pause:
        bouton_pause.configure(text="Relancer")
    else:
        bouton_pause.configure(text="Pause")


def verifier_alarme():
    """ Vérifie si l'heure actuelle correspond à l'alarme """
    global heure, alarme
    if alarme and heure == alarme:
        # Jouer le son de l'alarme
        son_alarme.play()
        messagebox.showinfo("HO REVEIL TOI, T'A RATE TA VIE")
        alarme = None  # Réinitialiser l'alarme après déclenchement


def changer_mode_affichage():
    """ Permet de changer le mode d'affichage entre 12h et 24h """
    global mode_12h
    mode_12h = not mode_12h
    if mode_12h:
        bouton_mode.configure(text="Mode 24h")
    else:
        bouton_mode.configure(text="Mode 12h")


def loop_horloge():
    """ Boucle principale pour mettre à jour l'heure """
    global horloge_en_pause
    while True:
        if not horloge_en_pause:
            incrementer_heure()
            afficher_heure()
            verifier_alarme()
        time.sleep(1)


# Création de la fenêtre principale
root = ctk.CTk()
root.title("Horloge et Alarme")
root.geometry("400x400")

# Label pour afficher l'heure
label_heure = ctk.CTkLabel(root, font=("Arial", 40, "bold"), text_color="cyan")
label_heure.pack(pady=20)

# Bouton pour mettre en pause / relancer l'horloge
bouton_pause = ctk.CTkButton(root, text="Pause", command=mettre_en_pause, width=200)
bouton_pause.pack(pady=10)

# Bouton pour changer le mode d'affichage
bouton_mode = ctk.CTkButton(root, text="Mode 12h", command=changer_mode_affichage, width=200)
bouton_mode.pack(pady=10)

# Boutons pour régler l'heure et l'alarme
button_regler_heure = ctk.CTkButton(root, text="Réglage Heure", command=regler_heure, width=200)
button_regler_heure.pack(pady=10)

button_regler_alarme = ctk.CTkButton(root, text="Réglage Alarme", command=regler_alarme, width=200)
button_regler_alarme.pack(pady=10)

# Initialiser l'heure avec l'heure actuelle
heure = (datetime.now().hour, datetime.now().minute, datetime.now().second)

# Lancer le thread pour la boucle horloge
thread_horloge = threading.Thread(target=loop_horloge, daemon=True)
thread_horloge.start()

# Lancer l'interface graphique
root.mainloop()