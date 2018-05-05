from dto import *
from enumy import *

# wartosci wejsciowe
max_working_hours = 140  # maksymalna liczba godzin dla pracownika
max_budget = 100000  # maksymalny budzet uczelni

Przedmioty = [
    Przedmiot(nazwa="POBO", dziedzina=Dziedzina.POL, typ=TypJednostkiDyd.LAB, liczba_godzin=4),
    Przedmiot(nazwa="POBO", dziedzina=Dziedzina.POL, typ=TypJednostkiDyd.WYKLAD, liczba_godzin=2),
    Przedmiot(nazwa="SKM", dziedzina=Dziedzina.CHEM, typ=TypJednostkiDyd.LAB, liczba_godzin=4),
    Przedmiot(nazwa="ZAH", dziedzina=Dziedzina.CHEM, typ=TypJednostkiDyd.WYKLAD, liczba_godzin=3),
    Przedmiot(nazwa="ZAH", dziedzina=Dziedzina.CHEM, typ=TypJednostkiDyd.LAB, liczba_godzin=5),
    Przedmiot(nazwa="SNR", dziedzina=Dziedzina.CHEM, typ=TypJednostkiDyd.LAB, liczba_godzin=2),
    Przedmiot(nazwa="SNR", dziedzina=Dziedzina.CHEM, typ=TypJednostkiDyd.WYKLAD, liczba_godzin=4),
    Przedmiot(nazwa="ZPI", dziedzina=Dziedzina.FIZ, typ=TypJednostkiDyd.LAB, liczba_godzin=3),
    Przedmiot(nazwa="ZPI", dziedzina=Dziedzina.FIZ, typ=TypJednostkiDyd.WYKLAD, liczba_godzin=2)
]
