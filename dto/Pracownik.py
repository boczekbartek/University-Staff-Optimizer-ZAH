from enumy import *

max_working_hours = 600

Jakosc = {
    StanowiskoPracownika.DOKTORANT: 1,
    StanowiskoPracownika.ADIUNKT: 2,
    StanowiskoPracownika.PROFESOR: 4
}

Pensje = {
    StanowiskoPracownika.DOKTORANT: 1,
    StanowiskoPracownika.ADIUNKT: 2,
    StanowiskoPracownika.PROFESOR: 4
}


class Pracownik:
    def __init__(self, stanowisko, dziedzina, id):
        self.stanowisko = stanowisko
        self.dziedzina = dziedzina
        self.pensja = Pensje[stanowisko]
        self.max_godzin = max_working_hours
        self.id = id
