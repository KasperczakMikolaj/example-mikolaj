class Trojkat:
    def __init__ (self, a, b, c, h_a):
        self.bok_a = a
        self.b = b
        self.c = c
        self.h_a = h_a
        # self.obwod = a + b +c
    
    def obwod(self):
        return self.bok_a + self.b + self.c
    
    def pole(self):

        return (self.bok_a * self.h_a)/2
    

trojkat_rownoboczny = Trojkat(10, 10, 10, 8)
trojkat_mikolaja = Trojkat(8, 6, 10, 4)
print(trojkat_rownoboczny.obwod())
print(trojkat_mikolaja.pole())


class Kwadrat:
    def __init__ (self, a):
        self.bok_a = a

    def obwod(self):
        return (self.bok_a * 4)
    
    def pole(self):
        return (self.bok_a ** 2)

kwadrat_mikolaja = Kwadrat(12)
print(kwadrat_mikolaja.obwod())
print(kwadrat_mikolaja.pole())

print("========================================================")

class Student:
    def __init__ (self, imie, nazwisko, numer_indeksu):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_indeksu = numer_indeksu
        self.oceny = []
    def __str__(self):
        return f"{self.imie} {self.nazwisko} {self.numer_indeksu}"
    
    def __int__(self):
        return 5
    
    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena)

    def zwroc_srednia(self):
        return sum(self.oceny) / len(self.oceny)
    
student_mikolaj = Student("Mikołaj", "Kasperczak","121119")
student_mikolaj.dodaj_ocene(4.5)
student_mikolaj.dodaj_ocene(5)
print(student_mikolaj.oceny)
print(student_mikolaj.zwroc_srednia())


print("========================================================")

class Samochody:
    def __init__(self, marka, model, typ_nadwozia, silnik, kolor, wersja_wyposazenia, rocznik):
        self.marka = marka
        self.model = model
        self.typ_nadwozia = typ_nadwozia
        self.silnik = silnik
        self.kolor = kolor
        self.wersja_wyposazenia = wersja_wyposazenia
        self.rocznik = rocznik

    def __str__(self):
        return f"{self.marka} {self.model} {self.typ_nadwozia} {self.silnik} {self.kolor} {self.wersja_wyposazenia} {self.rocznik}"
    
    def __int__(self):
        return 10
    
samochod_moj = Samochody("Ford", "Mondeo", "Hatchback", "1.6_benzyna", "czarny", "Ghia", "2014")
print(samochod_moj)

    

