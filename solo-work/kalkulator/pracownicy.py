import csv

class Pracownik:
    def __init__(self, imie, nazwisko, wynagrodzenie_brutto):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wynagrodzenie_brutto = float(wynagrodzenie_brutto)

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"

    def zarobki_brutto(self):
        return self.wynagrodzenie_brutto

    def wynik_wynagrodzenie_netto(self):
        return self.wynagrodzenie_brutto * 0.77

    def wynik_calkowity_koszt(self):
        return self.wynagrodzenie_brutto * 1.17

    @staticmethod
    def wynik_calkowity_koszt_pracodawcy(pracownicy):
        return sum(pracownik.wynik_calkowity_koszt() for pracownik in pracownicy)

def wczytaj_pracownikow(sciezka):
    pracownicy = []
    with open(sciezka, 'r', newline='') as plik_csv:
        arkusz_csv = csv.DictReader(plik_csv)
        for wiersz in arkusz_csv:
            imie = wiersz['imie']
            nazwisko = wiersz['nazwisko']
            wynagrodzenie_brutto = wiersz['wynagrodzenie_brutto']
            pracownik = Pracownik(imie, nazwisko, wynagrodzenie_brutto)
            pracownicy.append(pracownik)
    return pracownicy

def wypisz_pracownikow(pracownicy):
    for pracownik in pracownicy:
        print(f"Pracownik: {pracownik}")
        print(f"Wartość brutto: {pracownik.zarobki_brutto()}")
        print(f"Wartość netto: {pracownik.wynik_wynagrodzenie_netto()}")
        print(f"Koszty pracodawcy: {pracownik.wynik_calkowity_koszt()}")
        print("---")

def oblicz_sume_kosztow(pracownicy):
    return Pracownik.wynik_calkowity_koszt_pracodawcy(pracownicy)

pracownicy = wczytaj_pracownikow(r'C:\Users\tzdra\example-project\solo-work\kalkulator\pracownik.csv')
wypisz_pracownikow(pracownicy)
suma_kosztow = oblicz_sume_kosztow(pracownicy)
print(f"Suma kosztów wynagrodzeń: {suma_kosztow}")