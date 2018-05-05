# coding: utf-8

# In[0]:
from dto import *
from enumy import *
from input_data import *

from scipy.optimize import minimize, rosen, rosen_der
from .Solution import Solution

a = Solution(alfa=2, beta=2, wsp_pasujacej_jakosci=1, wsp_niepasujacej_jakosci=0.1)
a.dodaj_dopasowanie(przedmiot=Przedmioty[0], pracownik=Pracownik(StanowiskoPracownika.PROFESOR, Dziedzina.POL))

# In[1]:
x0 = [1.3, 0.7, 0.8, 1.9, 1.2]
res = minimize(rosen, x0, method='BFGS', jac=rosen_der, options={'gtol': 1e-6, 'disp': True})

print(res.x)

print(res.message)

# In[2]:
c = [-1, 4]
A = [[-3, 1], [1, 2]]
b = [6, 4]
x0_bounds = (None, None)
x1_bounds = (-3, None)
from scipy.optimize import linprog
res = linprog(c, A_ub=A, b_ub=b, bounds=(x0_bounds, x1_bounds),
              options={"disp": True})

import numpy as np

dopasowanie = np.array([
    # ZAH_LAB ZAH_WYKLAD SOI_LAB SOI_WYKKLAD
    [1, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0],
    [1, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0],   # ograniczenie
    [0, 0, 0, 0, 0, 0],
])


def fun_celu(dopasowanie: np.array) -> float:
    for
