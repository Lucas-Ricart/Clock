from datetime import datetime
import time
import os

os.system('cls')
while True :
    choix=input("Utiliser l'heure actuelle ? (o/n) :")
    if choix == 'N' or choix == 'n' :
        while True :
            horloge = input("(hh:mm:ss) : ")
            heures,minutes,secondes = map(int,horloge.split(':'))
            if 0 <= heures < 24 and 0 <= minutes < 60 and 0 <= secondes < 60 :
                os.system('cls')
                print(f'{heures:02}:{minutes:02}:{secondes:02}')
                while True :
                    time.sleep(1)
                    os.system('cls')
                    secondes += 1
                    if secondes == 60:
                        secondes = 0
                        minutes += 1
                    if minutes == 60:
                        minutes = 0
                        heures += 1
                    if heures == 24:
                        heures = 0
                    print(f'{heures:02}:{minutes:02}:{secondes:02}')
            else :
                print('Error ! Again !')
    elif choix == 'O' or choix == 'o' :
        while True :
            os.system('cls')
            horloge=datetime.now()
            print(f'{horloge.hour:02}:{horloge.minute:02}:{horloge.second:02}')
            time.sleep(1)