from dto import *
from enumy import *

import pandas as pd
# wartosci wejsciowe
max_budget = 8  # maksymalny budzet uczelni
max_czas = 8

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

Pracownicy = [
    Pracownik(StanowiskoPracownika.PROFESOR, Dziedzina.POL, 1),
    Pracownik(StanowiskoPracownika.PROFESOR, Dziedzina.CHEM, 2),
    Pracownik(StanowiskoPracownika.PROFESOR, Dziedzina.FIZ, 3),
    Pracownik(StanowiskoPracownika.PROFESOR, Dziedzina.MAT, 4),
    Pracownik(StanowiskoPracownika.PROFESOR, Dziedzina.POL, 5),
    Pracownik(StanowiskoPracownika.PROFESOR, Dziedzina.CHEM, 6),
    Pracownik(StanowiskoPracownika.PROFESOR, Dziedzina.FIZ, 7),
    Pracownik(StanowiskoPracownika.PROFESOR, Dziedzina.MAT, 8)
]


def save_to_csv(przedmioty, pracownicy):
    df_pracownicy = pd.DataFrame([pracownik.to_dict() for pracownik in pracownicy])
    df_przedmioty = pd.DataFrame([przedmiot.to_dict() for przedmiot in przedmioty])

    df_pracownicy.to_csv("Pracownicy.csv", index=False)
    df_przedmioty.to_csv("Przedmioty.csv", index=False)


def load_pracownicy(filename):
    df = pd.read_csv(filename)
    res = []

    for _, pracownik in df.iterrows():
        res.append(
            Pracownik(dziedzina=Dziedzina(pracownik.dziedzina),
                      stanowisko=StanowiskoPracownika(pracownik.stanowisko),
                      id=pracownik.id)
        )

    return res


def load_przedmioty(filename):
    df = pd.read_csv(filename)
    res = []

    for _, przedmiot in df.iterrows():
        res.append(
            Przedmiot(dziedzina=Dziedzina(przedmiot.dziedzina),
                      liczba_godzin=int(przedmiot.liczba_godzin),
                      nazwa=przedmiot.nazwa,
                      typ=TypJednostkiDyd(przedmiot.typ)
                      )
        )

    return res
