from enumy import *

class JednostkaDydaktyczna:
    def __init__(self, dziedzina, liczba_godzin, typ, nazwa, nauczyciel):
        self.nauczyciel = nauczyciel
        self.dziedzina = dziedzina
        self.liczba_godzin = liczba_godzin
        self.typ = typ
        self.nazwa = nazwa
