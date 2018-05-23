from pulp import *
from enumy import *
from input_data import *

from scipy.optimize import minimize
from model.Solution import *

objs = [2,3,2,5,3]
weights = [1,2,2,1,3]
knapweight = 5

Przedmioty = [
    Przedmiot(nazwa="POBO", dziedzina=Dziedzina.POL, typ=TypJednostkiDyd.LAB, liczba_godzin=4),
    Przedmiot(nazwa="POBO2", dziedzina=Dziedzina.POL, typ=TypJednostkiDyd.WYKLAD, liczba_godzin=2),
    Przedmiot(nazwa="SKM", dziedzina=Dziedzina.CHEM, typ=TypJednostkiDyd.LAB, liczba_godzin=4),
    Przedmiot(nazwa="ZAH", dziedzina=Dziedzina.CHEM, typ=TypJednostkiDyd.WYKLAD, liczba_godzin=3),
    Przedmiot(nazwa="ZAH2", dziedzina=Dziedzina.CHEM, typ=TypJednostkiDyd.LAB, liczba_godzin=5),
    Przedmiot(nazwa="SNR", dziedzina=Dziedzina.CHEM, typ=TypJednostkiDyd.LAB, liczba_godzin=2),
    Przedmiot(nazwa="SNR2", dziedzina=Dziedzina.CHEM, typ=TypJednostkiDyd.WYKLAD, liczba_godzin=4),
    Przedmiot(nazwa="ZPI2", dziedzina=Dziedzina.FIZ, typ=TypJednostkiDyd.LAB, liczba_godzin=3),
    Przedmiot(nazwa="ZPI", dziedzina=Dziedzina.FIZ, typ=TypJednostkiDyd.WYKLAD, liczba_godzin=2)
]

Pracownicy = [
    Pracownik(StanowiskoPracownika.PROFESOR, Dziedzina.POL, 1),
    Pracownik(StanowiskoPracownika.DOKTORANT, Dziedzina.CHEM, 2),
    Pracownik(StanowiskoPracownika.DOKTORANT, Dziedzina.FIZ, 3),
    Pracownik(StanowiskoPracownika.PROFESOR, Dziedzina.MAT, 4),
    Pracownik(StanowiskoPracownika.ADIUNKT, Dziedzina.POL, 5),
    Pracownik(StanowiskoPracownika.ADIUNKT, Dziedzina.CHEM, 6),
    Pracownik(StanowiskoPracownika.DOKTORANT, Dziedzina.FIZ, 7),
    Pracownik(StanowiskoPracownika.PROFESOR, Dziedzina.MAT, 8)
]
model = Solution(alfa=2, beta=-2, wsp_pasujacej_jakosci=1, wsp_niepasujacej_jakosci=0.1)
res = []
for pracownik in Pracownicy:
    for przedmiot in Przedmioty:
        res.append(
            model.alfa * model.oblicz_jakosc_pracownika(pracownik, przedmiot) - model.beta * pracownik.pensja)

prob = LpProblem('Knapsack', LpMaximize)
prob2 = LpProblem("ZAH", LpMinimize)
xs2 = [LpVariable("x{}".format(i+1), cat="Binary") for i in range(len(res))]
xs = [LpVariable("x{}".format(i+1), cat="Binary") for i in range(len(objs))]

# add objective
total_prof2 = sum(x * obj for x,obj in zip(xs2, res))
prob2 += total_prof2
# add objective
total_prof = sum(x * obj for x,obj in zip(xs, objs))
prob += total_prof

# add constraint
total_weight = sum(x * w for x, w in zip(xs, weights))
prob += total_weight <= knapweight

status = prob.solve()
print(LpStatus[status])
print("Objective value:", value(prob.objective))
print ('\nThe values of the variables : \n')
for v in prob.variables():
    print(v.name, "=", v.varValue)