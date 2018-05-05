from enumy import *

class Przedmiot:
    def __init__(self, nazwa, dziedzina, typ, liczba_godzin):
        self.liczba_godzin = liczba_godzin
        self.typ = typ
        self.dziedzina = dziedzina
        self.nazwa = nazwa
