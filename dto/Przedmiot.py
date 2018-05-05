class Przedmiot:
    def __init__(self, nazwa, dziedzina, typ, liczba_godzin):
        self.liczba_godzin = liczba_godzin
        self.typ = typ
        self.dziedzina = dziedzina
        self.nazwa = nazwa

    def to_dict(self):
        return dict(liczba_godzin = self.liczba_godzin,
                    typ=self.typ.value,
                    dziedzina=self.dziedzina.value,
                    nazwa=self.nazwa
                    )

    def get_id(self):
        return self.nazwa + self.dziedzina
