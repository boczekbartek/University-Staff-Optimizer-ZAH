from dto import *
import numpy as np


class Solution:
    def __init__(self, wsp_pasujacej_jakosci, wsp_niepasujacej_jakosci, alfa=1, beta=-1):
        self.wsp_pasujacej_jakosci = wsp_pasujacej_jakosci
        self.wsp_niepasujacej_jakosci = wsp_niepasujacej_jakosci
        self.beta = beta
        self.alfa = alfa
        self.mapa_dopasowan_przedmiot_pracownik = {}

    def dodaj_dopasowanie(self, przedmiot, pracownik):
        self.mapa_dopasowan_przedmiot_pracownik[przedmiot] = pracownik

    def pobierz_przypisanego_pracownika(self, przedmiot):
        return self.mapa_dopasowan_przedmiot_pracownik[przedmiot]

    def oblicz_jakosc_pracownika(self, pracownik, przedmiot):
        if przedmiot.dziedzina == pracownik.dziedzina:
            mnoznik_jakosci = self.wsp_pasujacej_jakosci
        else:
            mnoznik_jakosci = self.wsp_niepasujacej_jakosci
        jakosc = mnoznik_jakosci * Jakosc[pracownik.stanowisko]
        return jakosc

    def funkcja_jakosci(self):
        jakosc = 0
        for (przedmiot, pracownik) in self.mapa_dopasowan_przedmiot_pracownik.items():
            jakosc = jakosc + self.oblicz_jakosc_pracownika(pracownik, przedmiot)
        return jakosc

    def funkcja_kosztu(self):
        koszt = 0
        for pracownik in set(self.mapa_dopasowan_przedmiot_pracownik.values()):
            koszt = koszt + pracownik.pensja
        return koszt

    def funkcja_celu(self) -> float:
        return self.alfa * self.funkcja_jakosci() + self.beta * self.funkcja_kosztu()

    # TODO
    def parse_input_data(self, przedmioty, pracownicy) -> np.array:
        """
        :param przedmioty:
        :param pracownicy:
        :return: wartosc poczatkowa -
                randomowa macierz z wierszami (pracownik.id) x (przedmiot.nazwa + przedmiot.typ_jednostki)
        """
        pass

    # TODO
    def optimize_scenario(self, encoded_array: np.array):
        """
        :param encoded_array: losowy scenariusz dopasowania
        :return: wartosc funkcji celu
        """
        # return optymalizator.optimize(encoded_array)
        pass
