from datetime import datetime
import time
import os

heure_alarme = 99
minute_alarme = 99
seconde_alarme = 99

def horloge(heure, minute, seconde, heure_alarme, minute_alarme, seconde_alarme) :
    os.system('cls')
    print(f'{heure:02}:{minute:02}:{seconde:02}')
    while True :
        if heure == heure_alarme and minute == minute_alarme and seconde == seconde_alarme-1:
            for i in range(60) :
                heure, minute, seconde = incrementer(heure, minute, seconde)
                time.sleep(1)
                os.system('cls')
                print(f'{heure:02}:{minute:02}:{seconde:02}')
                print("DRING DRING! C'est l'heure.")
        else :
            heure, minute, seconde = incrementer(heure, minute, seconde)
            time.sleep(1)
            os.system('cls')
            print(f'{heure:02}:{minute:02}:{seconde:02}')

def choix() :
    test = 0
    while True :
        os.system('cls')
        if test > 3 :
            print('Erreur. Rééssayer.')
        print("1. Lancer l'horloge")
        print("2. Régler l'heure")
        print("3. Régler une alarme")
        test=int(input())
        if test == 1 or test == 2 or test == 3 :
            return test
        
def incrementer(heure, minute, seconde) :
    seconde += 1
    if seconde == 60 :
         seconde = 0
         minute += 1
    if minute == 60 :
        minute = 0
        heure += 1
    if heure == 24 :
        heure = 0
    return heure, minute, seconde
                   
def heure_machine() :
    while True :
        os.system('cls')
        maintenant=datetime.now()
        return maintenant.hour, maintenant.minute, maintenant.second

def afficher_heure() :
    while True :
        horloge = input("(hh:mm:ss) : ")
        try :
            heure, minute, seconde = map(int,horloge.split(':'))
            if 0 <= heure < 24 and 0 <= minute < 60 and 0 <= seconde < 60 :
                return heure, minute, seconde
            else :
                print('Erreur. Rééssayer.')
        except ValueError :
            os.system('cls')
            print('Erreur. Rééssayer.')

def définir_alarme() :
    while True :
        horloge = input("(hh:mm:ss) : ")
        try :
            heure, minute, seconde = map(int,horloge.split(':'))
            if 0 <= heure < 24 and 0 <= minute < 60 and 0 <= seconde < 60 :
                return heure, minute, seconde
            else :
                print('Erreur. Rééssayer.')
        except ValueError :
            os.system('cls')
            print('Erreur. Rééssayer.')

test=choix()
heure, minute, seconde = heure_machine()
if test == 2 :
    heure, minute, seconde = afficher_heure()
elif test == 3 :
    heure_alarme, minute_alarme, seconde_alarme = définir_alarme()
horloge(heure, minute, seconde, heure_alarme, minute_alarme, seconde_alarme)