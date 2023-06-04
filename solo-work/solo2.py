class Samochody:
    def __init__(self, marka, model, typ_nadwozia, silnik, kolor, wersja_wyposazenia, rocznik, przebieg):
        self.marka = marka
        self.model = model
        self.typ_nadwozia = typ_nadwozia
        self.silnik = silnik
        self.kolor = kolor
        self.wersja_wyposazenia = wersja_wyposazenia
        self.rocznik = rocznik
        self.przebieg = przebieg
        self.cena = []
    
    def __str__(self):
        return f"{self.marka} {self.model} {self.typ_nadwozia} {self.silnik} {self.kolor} {self.wersja_wyposazenia} {self.rocznik} {self.przebieg}"
    
    def dodaj_cena(self, cena):
        self.cena.append(cena)
    
    def zwroc_srednia_cena(self):
        return sum(self.cena) /len(self.cena)
    
samochod_moj = Samochody("Ford", "Mondeo", "Hatchback", "1.6_benzyna", "czarny", "Ghia", "2014", "103000 km")
samochod_moj.dodaj_cena(100000)
print(samochod_moj)
print(samochod_moj.cena)

    

