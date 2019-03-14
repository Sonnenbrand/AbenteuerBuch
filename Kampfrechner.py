
"""
Dies ist ein Rechner um Kämpfe im Buch Einsamer Wolf schnell zu rechnen.
Erst eine kurze Abfrage der eigenen Stärke und Ausdauer.
Dann eine Enstcheidung im zu Kämpfen oder den Status zu sehen.
To do:
    - Kampftabelle https://mantikoreverlag.de/wp-content/uploads/downloads/1/EW_Kampftabelle.pdf
      muss noch abgebildet werden.
      Alt: Aktuelle Lösung If / Elif Schleife über die Tabelle gehen lassen.
      Neuer Ansatz: JSON File oder CSV Tabelle einlesen
Stand 01.03.2019
"""


import random

HeldenName = input("Wie heißt du? ")
HeldenKraft = int((input("Wie hoch ist deine Kraft? ")))
HeldenAusdauer = int((input("Wie ist deine Ausdauer? ")))
HeldenKA = [HeldenKraft, HeldenAusdauer]
Heldlebtnoch = True
IstMonsterTot = False
Zufallszahl = 1 # random.randint(-1, 10)

print ("Alles klar " + HeldenName + "!")

def heldenstatus():
    print("Du hast " + str(HeldenAusdauer) + " als Ausdauer und du hast " + str(HeldenKraft) + " als Kraft.")

HeldenEntscheidung = int(input("Was willst du tun? \n1 = Wie ist mein Status?\n2 = Ich muss kämpfen!\n"))

def kampfergebniss(KampfQoutient, Zufallszahl, HeldenAusdauer):
    if KampfQoutient <= -9 and Zufallszahl == 1:
        print("Du bist Tod!")
    elif KampfQoutient == -8 and Zufallszahl == 1:
        HeldenAusdauer = HeldenAusdauer - 8
        print("Das tat weh...deine Ausdauer ist um 8 Punkte auf " + str(HeldenAusdauer) + " gesunken!")
    elif KampfQoutient == -7 and Zufallszahl == 1:
        Ergebniss = HeldenAusdauer - 8
        print("Das tat weh...deine Ausdauer ist um 8 Punkte auf " + str(Ergebniss) + " gesunken!")
    elif KampfQoutient == -6 and Zufallszahl == 1:
        Ergebniss = HeldenAusdauer - 6
        print("Das tat weh...deine Ausdauer ist um 6 Punkte auf " + str(Ergebniss) + " gesunken!")
    else:
        print("Das war knapp!")

if HeldenEntscheidung == 1:
    heldenstatus()
else:
    print("Auf in die Schlacht!")
    MonsterKraft = 10 # int(input("Wie ist die Kraft des Monsters? "))
    MonsterAusdauer = 5 # int(input("Wie ist die Ausdauer des Monsters? "))
    KampfQoutient = HeldenKraft - MonsterKraft
    kampfergebniss(KampfQoutient, Zufallszahl, HeldenAusdauer)
