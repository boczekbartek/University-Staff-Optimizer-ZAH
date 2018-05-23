# coding: utf-8

# In[0]:
from dto import *
from enumy import *
from input_data import *

from scipy.optimize import minimize
from model.Solution import *

if __name__ == '__main__':
    dopasowanie = np.array([
        # ZAH_LAB ZAH_WYKLAD SOI_LAB SOI_WYKKLAD
        [1, 1, 1, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],  # ograniczenie
    ])

    mapa_przedmiotow = {
        0: Przedmiot(nazwa="POBO", dziedzina=Dziedzina.POL, typ=TypJednostkiDyd.LAB, liczba_godzin=4),
        1: Przedmiot(nazwa="POBO", dziedzina=Dziedzina.POL, typ=TypJednostkiDyd.WYKLAD, liczba_godzin=2),
        2: Przedmiot(nazwa="SKM", dziedzina=Dziedzina.POL, typ=TypJednostkiDyd.LAB, liczba_godzin=4),
        3: Przedmiot(nazwa="ZAH", dziedzina=Dziedzina.POL, typ=TypJednostkiDyd.WYKLAD, liczba_godzin=3)}
    mapa_pracownikow = {0: Pracownik(StanowiskoPracownika.PROFESOR, Dziedzina.POL, 1),
                        1: Pracownik(StanowiskoPracownika.ADIUNKT, Dziedzina.POL, 2),
                        2: Pracownik(StanowiskoPracownika.ADIUNKT, Dziedzina.POL, 3),
                        3: Pracownik(StanowiskoPracownika.DOKTORANT, Dziedzina.POL, 4)}


    def de_flatten(vec, columns):
        return fun_celu(vec.reshape(-1, columns))


    def fun_celu(dopasowanie: np.array) -> float:
        model = Solution(alfa=2, beta=-2, wsp_pasujacej_jakosci=1, wsp_niepasujacej_jakosci=0.1)
        for y, row in enumerate(dopasowanie):
            for x, cell in enumerate(row):
                if cell != 0:
                    model.dodaj_dopasowanie(mapa_przedmiotow[x], mapa_pracownikow[y])
        print("Fun_celu:", model.funkcja_celu())
        return model.funkcja_celu()


    def ograniczenie_koszt(matrix):
        suma = 0
        for y, row in enumerate(matrix):
            for x, cell in enumerate(row):
                if cell != 0:
                    suma += mapa_pracownikow[y].pensja
        print("Koszt:", suma)
        return suma


    def ograniczenie_czas(row):
        # for y, row in enumerate(matrix):
        czas_pracownika = 0
        for x, cell in enumerate(row):
            if cell != 0:
                czas_pracownika += mapa_przedmiotow[x].liczba_godzin
        print("Czas:", czas_pracownika)
        return czas_pracownika

    from functools import partial

    opt_fun = partial(de_flatten, columns=4)
    bnds = tuple([(0, 1) for i in range(dopasowanie.shape[0] * dopasowanie.shape[1])])

    cons = [
        {'type': 'ineq', 'fun': lambda x: max_budget - ograniczenie_koszt(x.reshape(-1, 4))},

        {'type': 'ineq', 'fun': lambda x: max_czas - ograniczenie_czas(x.reshape(-1, 4)[0])},
        {'type': 'ineq', 'fun': lambda x: max_czas - ograniczenie_czas(x.reshape(-1, 4)[1])},
        {'type': 'ineq', 'fun': lambda x: max_czas - ograniczenie_czas(x.reshape(-1, 4)[2])},
        {'type': 'ineq', 'fun': lambda x: max_czas - ograniczenie_czas(x.reshape(-1, 4)[3])},

        {'type': 'ineq', 'fun': lambda x: 1 - np.sum(x.reshape(-1, 4).T[0])},
        {'type': 'ineq', 'fun': lambda x: 1 - np.sum(x.reshape(-1, 4).T[1])},
        {'type': 'ineq', 'fun': lambda x: 1 - np.sum(x.reshape(-1, 4).T[2])},
        {'type': 'ineq', 'fun': lambda x: 1 - np.sum(x.reshape(-1, 4).T[3])}
    ]

    cons = tuple(cons)
    for i in cons:
        print(i)

    res = minimize(opt_fun, dopasowanie.flatten(), method='COBYLA', tol=1e-6, bounds=bnds, constraints=cons)

    print("Dopasowanie", res.x.reshape(-1, 4))
    print("Fun celu", fun_celu(res.x.reshape(-1, 4)))
    print("Koszt ", ograniczenie_koszt(res.x.reshape(-1, 4)))
    for row in res.x.reshape(-1, 4):
        print("Czas" , ograniczenie_czas(row))
    for col in res.x.reshape(-1, 4).T:
        print("Suma realizacji", np.sum(col))
