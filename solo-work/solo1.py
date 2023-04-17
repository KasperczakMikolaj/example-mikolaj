# zadanie 1.1
hello = "Hello"
student = "Mikolaj"

print("{} {}".format(hello, student))

# zadanie 1.2
student = input("Wpisz swoje imie: ")
print("Hello {}".format(student))

# zadanie 1.3

studenci = ["Ania", "Kuba", "Piotr", "Jan"]

liczba_studentow = len(studenci)
print("Liczba studentow wynosi:", liczba_studentow)

# zadanie 1.4

studenci = ["Ania", "Kasia", "Piotr", "Tomek"]

for student in studenci:
    print("Hello {}".format(student))


# zadanie 1.5

liczba = 3
potega = 4

wynik = liczba ** potega

print("Wynik wynosi:", wynik)


# zadanie 1.6

ciag_znakow = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"
liczba_nawiasow_otwierajacych = 0

for znak in ciag_znakow:
    if znak == "(":
        liczba_nawiasow_otwierajacych += 1

print("Liczba nawiasow otwierajacych wynosi:", liczba_nawiasow_otwierajacych)
