

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

# Hier die Variablendefinitionen. Das Dictionary müsste zur lesbarkeit anders dargestellt werden.

HeldenKraft = int((input("Wie hoch ist deine Kraft? ")))
HeldenAusdauer = int((input("Wie ist deine Ausdauer? ")))
KampfErgebnisseF = {
    "0-11": -6,
    "0-10": -7,
    "0-9": -7,
    "0-8": -8,
    "0-7": -8,
    "0-6": -9,
    "0-5": -9,
    "0-4": -10,
    "0-3": -10,
    "0-2": -11,
    "0-1": -11,
    "0-0": -12,
    "00": -12,
    "01": -14,
    "02": -14,
    "03": -16,
    "04": -16,
    "05": -18,
    "06": -18,
    "07": -99,
    "08": -99,
    "09": -99,
    "010": -99,
    "011": -99,

    "1-11": -0,
    "1-10": -0,
    "1-9": -0,
    "1-8": -0,
    "1-7": -0,
    "1-6": -0,
    "1-5": -0,
    "1-4": -1,
    "1-3": -1,
    "1-2": -2,
    "1-1": -2,
    "1-0": -3,
    "10": -3,
    "11": -4,
    "12": -4,
    "13": -5,
    "14": -5,
    "15": -6,
    "16": -6,
    "17": -7,
    "18": -7,
    "19": -8,
    "110": -8,
    "111": -9,
} # TODO: Dictionaries vervvollständigen
KampfErgebnisseH = {
    "0-11": -0,
    "0-10": -0,
    "0-9": -0,
    "0-8": -0,
    "0-7": -0,
    "0-6": -0,
    "0-5": -0,
    "0-4": -0,
    "0-3": -0,
    "0-2": -0,
    "0-1": -0,
    "0-0": -0,
    "00": -0,
    "01": -0,
    "02": -0,
    "03": -0,
    "04": -0,
    "05": -0,
    "06": -0,
    "07": -0,
    "08": -0,
    "09": -0,
    "010": -0,
    "011": -0,

    "1-11": -99,
    "1-10": -99,
    "1-9": -99,
    "1-8": -8,
    "1-7": -8,
    "1-6": -6,
    "1-5": -6,
    "1-4": -6,
    "1-3": -6,
    "1-2": -5,
    "1-1": -5,
    "1-0": -5,
    "10": -5,
    "11": -5,
    "12": -5,
    "13": -4,
    "14": -4,
    "15": -4,
    "16": -4,
    "17": -4,
    "18": -4,
    "19": -3,
    "110": -3,
    "111": -3,
}
Zufallszahl = 1 # TODO: Random Kommentar entfernen random.randint(0, 2)
Teil1 = 0


# Hier beginnt das Programm

def kampf_H(KampfQuotient, Zufallszahl, HeldenAusdauer):
    Teil1 = str(Zufallszahl) + str(KampfQoutient)
    HeldenAusdauer = HeldenAusdauer + KampfErgebnisseH[Teil1]
    return HeldenAusdauer

def kampf_M(KampfQoutient, Zufallszahl, MonsterAusdauer):
    Teil1 = str(Zufallszahl) + str(KampfQoutient)
    MonsterAusdauer = MonsterAusdauer + KampfErgebnisseF[Teil1]
    return MonsterAusdauer

MonsterKraft = int(input("Wie ist die Kraft des Monsters? "))
MonsterAusdauer = int(input("Wie ist die Ausdauer des Monsters? "))
print("Du hast also " + str(HeldenKraft) + " Kraft und " + str(HeldenAusdauer) + " Ausdauer.")
print("Dein Gegner hat " + str(MonsterKraft) + " Kraft und " + str(MonsterAusdauer) + " Ausdauer.")
print("Der Kampf beginnt!")
KampfQoutient = HeldenKraft - MonsterKraft
ErgbenissH = kampf_H(KampfQoutient, Zufallszahl, HeldenAusdauer)
ErgebnissM = kampf_M(KampfQoutient, Zufallszahl, MonsterAusdauer)
print("Heldenausdauer neu: " + str(ErgbenissH) + " - Monsterausdauer neu: " + str(ErgebnissM))