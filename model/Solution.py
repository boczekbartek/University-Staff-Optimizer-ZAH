from dto import *


class Solution:
    def __init__(self, alfa, beta, wsp_pasujacej_jakosci, wsp_niepasujacej_jakosci):
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

    def funkcja_jakosci(self, przedmioty, pracownicy):
        jakosc = 0
        for (przedmiot, pracownik) in self.mapa_dopasowan_przedmiot_pracownik:
            jakosc = jakosc + self.oblicz_jakosc_pracownika(pracownik, przedmiot)
        return jakosc

    def funkcja_kosztu(self, przedmioty, pracownicy):
        koszt = 0
        for pracownik in set(self.mapa_dopasowan_przedmiot_pracownik.values()):
            koszt = koszt + pracownik.pensja

    # funkcja optymalizowana, to pewnie do jakiegos optymalizatora trzeba machnac
    def fun_celu(self, jakosc, koszt):
        return self.alfa * jakosc + self.beta * koszt

