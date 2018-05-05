from dto import *
from model import *
from enumy import *
from input_data import *


if __name__ == '__main__':
    a = Solution(2, 2, 1, 0.1)
    print(a.oblicz_jakosc_pracownika(Pracownik(StanowiskoPracownika.PROFESOR, Dziedzina.POL), Przedmioty[0]))
