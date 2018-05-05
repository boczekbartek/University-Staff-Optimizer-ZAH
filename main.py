from dto import *
from model import *
from enumy import *
from input_data import *


if __name__ == '__main__':
    a = Solution(alfa=2, beta=2, wsp_pasujacej_jakosci=1, wsp_niepasujacej_jakosci=0.1)
    print(a.oblicz_jakosc_pracownika(Pracownik(StanowiskoPracownika.PROFESOR, Dziedzina.POL), Przedmioty[0]))
