from dto import *
from model import *
from enumy import *
from input_data import *


def test_funkcji_celu():
    a = Solution(alfa=2, beta=2, wsp_pasujacej_jakosci=1, wsp_niepasujacej_jakosci=0.1)
    a.dodaj_dopasowanie(przedmiot=Przedmioty[0], pracownik=Pracownik(StanowiskoPracownika.PROFESOR, Dziedzina.POL))
    assert a.funkcja_celu() == 16
