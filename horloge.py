import time
from datetime import datetime, timedelta
import datetime
import os

heure = None
alarme = None
APM = True
choix = False
pause = False

def afficher_heure():
    global heure
    heures, minutes, secondes = heure
    horloge = datetime.time(heures, minutes, secondes)
    os.system('cls')
    if APM:
        if heures < 12 :
            print(horloge.strftime('AM %I:%M:%S'))
        else :
            print(horloge.strftime('PM %I:%M:%S'))
    else :
        print(horloge.strftime('%H:%M:%S'))

def heure_actuelle() :
    global heure
    from datetime import datetime
    while True :
        heure = datetime.now()
        heure = (heure.hour, heure.minute, heure.second)
        return

def régler_heure() :
    global heure, choix
    while True:
        os.system('cls')
        try:
            if choix == True:
                heure = input('(hh:mm:ss) : ')
                heures, minutes, secondes = map(int, heure.split(":"))
                if 0 <= heures < 24 and 0 <= minutes < 60 and 0 <= secondes < 60:
                    heure = (heures, minutes, secondes)
                    return
                else:
                    print('Erreur. Réessayer.')
            elif choix == False:
                heure_actuelle()
                return
            else:
                print('Erreur. Réessayer.')
        except ValueError:
            print('Erreur. Réessayer.')
        
def régler_alarme() :
    global alarme
    while True:
        os.system('cls')
        try:
            alarme = input('(hh:mm:ss) : ')
            heures, minutes, secondes = map(int, alarme.split(":"))
            if 0 <= heures < 24 and 0 <= minutes < 60 and 0 <= secondes < 60:
                alarme = (heures, minutes, secondes)
                return
            else :
                print('Erreur. Réessayer.')
        except ValueError:
            print('Erreur. Réessayer.')

def test_alarme() :
    global alarme, heure
    if heure == alarme :
        for i in range(30) :
            afficher_heure()
            print("Dring Dring ! Il est l'heure !")
            time.sleep(1)

def incrémenter() :
    global heure, pause
    heures, minutes, secondes = heure
    while True :
        if pause == True :
            return
        else :
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
            return
    
def selection() :
    global choix, APM, pause
    test = 0
    while True :
        os.system('cls')
        print("1. Lancer l'horloge")
        if choix == False :
             print("2. Régler l'heure")
        else :
            print("2. Utiliser l'heure locale")
        print('3. Régler une alarme')
        if APM == False :
            print('4. Passer en format 12h')
        else :
            print('4. Passer en format 24h')
        if pause == False :
            print('5. Mettre en pause')
        else :
            print('5. Couper la pause')
        test=int(input())
        try :
            if test == 2 :
                if choix == False :
                    choix = True
                    régler_heure()
                else :
                    choix = False
                    régler_heure()
            elif test == 3 :
                régler_alarme()
            elif test == 4 :
                if APM == False :
                    APM = True
                else :
                    APM = False
            elif test == 5 :
                if pause == False :
                    pause = True
                else :
                    pause = False
            return
        except ValueError :
            print('Erreur. Réessayer.')
def main() :
    heure_actuelle()
    while True :
        selection()
        try :
            while True :
                afficher_heure()
                incrémenter()
                test_alarme()
                time.sleep(1)
        except KeyboardInterrupt :
            None


main()