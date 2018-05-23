# coding: utf-8

# In[0]:
from dto import *
from enumy import *
from input_data import *

from scipy.optimize import minimize, rosen, rosen_der
from model.Solution import *

if __name__ == '__main__':
    # a = Solution(alfa=2, beta=2, wsp_pasujacej_jakosci=1, wsp_niepasujacej_jakosci=0.1)
    # a.dodaj_dopasowanie(przedmiot=Przedmioty[0], pracownik=Pracownik(StanowiskoPracownika.PROFESOR, Dziedzina.POL, 123))
    #
    # # In[1]:
    # x0 = [1.3, 0.7, 0.8, 1.9, 1.2]
    # res = minimize(rosen, x0, method='BFGS', jac=rosen_der, options={'gtol': 1e-6, 'disp': True})
    #
    # print(res.x)
    #
    # print(res.message)
    #
    # # In[2]:
    # c = [-1, 4]
    # A = [[-3, 1], [1, 2]]
    # b = [6, 4]
    # x0_bounds = (None, None)
    # x1_bounds = (-3, None)
    # from scipy.optimize import linprog
    # res = linprog(c, A_ub=A, b_ub=b, bounds=(x0_bounds, x1_bounds), options={"disp": True})
    #
    # import numpy as np

    dopasowanie = np.array([
        # ZAH_LAB ZAH_WYKLAD SOI_LAB SOI_WYKKLAD
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],  # ograniczenie
    ])


    def de_flatten(vec, columns):
        return fun_celu(vec.reshape(-1, columns))


    def fun_celu(dopasowanie: np.array) -> float:
        # trzeba zrobic jakas mape indeks kolumny -> kod przedmiotu i indeks wiersza -> kod pracownika
        mapa_przedmiotow = {
            0: Przedmiot(nazwa="POBO", dziedzina=Dziedzina.POL, typ=TypJednostkiDyd.LAB, liczba_godzin=4),
            1: Przedmiot(nazwa="POBO", dziedzina=Dziedzina.POL, typ=TypJednostkiDyd.WYKLAD, liczba_godzin=2),
            2: Przedmiot(nazwa="SKM", dziedzina=Dziedzina.CHEM, typ=TypJednostkiDyd.LAB, liczba_godzin=4),
            3: Przedmiot(nazwa="ZAH", dziedzina=Dziedzina.CHEM, typ=TypJednostkiDyd.WYKLAD, liczba_godzin=3)}
        mapa_pracownikow = {0: Pracownik(StanowiskoPracownika.PROFESOR, Dziedzina.POL, 1),
                            1: Pracownik(StanowiskoPracownika.PROFESOR, Dziedzina.CHEM, 2),
                            2: Pracownik(StanowiskoPracownika.PROFESOR, Dziedzina.FIZ, 3),
                            3: Pracownik(StanowiskoPracownika.PROFESOR, Dziedzina.MAT, 4)}

        model = Solution(alfa=2, beta=2, wsp_pasujacej_jakosci=1, wsp_niepasujacej_jakosci=0.1)
        for y, row in enumerate(dopasowanie):
            for x, cell in enumerate(row):
                if cell != 0:
                    model.dodaj_dopasowanie(mapa_przedmiotow[x], mapa_pracownikow[y])
        print(model.funkcja_celu())
        return model.funkcja_celu()


    from functools import partial

    opt_fun = partial(de_flatten, columns=4)
    bnds = tuple([(0, 1) for i in range(dopasowanie.shape[0] * dopasowanie.shape[1])])

    def przekroczone_ograniczenie_koszt(matrix):
        suma = 0
        for y, row in enumerate(matrix):
            for x, cell in enumerate(row):
                if cell != 0:
                    suma = suma + mapa_pracownikow[y].pensja
        return suma > max_budget

    def przekroczone_ograniczenie_czas(matrix):
        for y, row in enumerate(matrix):
            czas_pracownika = 0
            for x, cell in enumerate(row):
                if cell != 0:
                    czas_pracownika = czas_pracownika + mapa_przedmiotow[x].liczba_godzin
            if(czas_pracownika > max_czas):
                return True
        return False


    cons = ({'type': 'ineq', 'fun': lambda x: x[0] - 2 * x[1] + 2},
            {'type': 'ineq', 'fun': lambda x: -x[0] - 2 * x[1] + 6},
            {'type': 'ineq', 'fun': lambda x: -x[0] + 2 * x[1] + 2})

    res = minimize(opt_fun, dopasowanie.flatten(), method='SLSQP', tol=1e-6, bounds=bnds)

    print(res.x.reshape(-1, 4))
