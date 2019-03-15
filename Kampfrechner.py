
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
Total Redo - Neuer Ansatz mit Dictionary und einfacher Schleife!
Stand 15.03.2019
"""

# import random

HeldenKraft = int((input("Wie hoch ist deine Kraft? ")))
HeldenAusdauer = int((input("Wie ist deine Ausdauer? ")))
KampfErgebnisseF = {"0-11":-6,"0-10":-7,"0-9":-7,"0-8":-8}
KampfErgebnisseH = {"0-11":-3,"0-10":-2,"0-9":-2,"0-8":-1}
Zufallszahl = str(0) # random.randint(-1, 10)
Teil1 = 1


if HeldenAusdauer > 0:
    print("Leben und kämpfen")
    MonsterKraft = 10 # int(input("Wie ist die Kraft des Monsters? "))
    MonsterAusdauer = 11 # int(input("Wie ist die Ausdauer des Monsters? "))
    KampfQoutient = HeldenKraft - MonsterKraft
    print("Ok, deine Ausdauer ist " + str(HeldenAusdauer) + " und das Monster hat noch " + str(MonsterAusdauer) + " !")
    Teil1 = str(Zufallszahl) + str(KampfQoutient)
    #ausdaueranpassungM(Teil1, MonsterAusdauer)
    MonsterAusdauer = MonsterAusdauer + KampfErgebnisseF[Teil1]
    HeldenAusdauer = HeldenAusdauer + KampfErgebnisseH[Teil1]
    print(MonsterAusdauer)

else:
    print("Tod")
