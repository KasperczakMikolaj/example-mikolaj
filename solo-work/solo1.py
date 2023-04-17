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


# zadanie 1.7


studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
studenci.sort(key=lambda x: x.split()[0]) 
print("Alfabetyczna lista studentow wynosi: ")
for student in studenci:
    print(student)



# zadanie 1.8

studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]

posortowani_studenci = sorted(studenci, key=lambda x: x.split()[-1])

print("Alfabetyczna lista studentow wynosi: ")
for student in posortowani_studenci:
    print(student)



# zadanie 1.9

studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]

liczba_n = 0
for student in studenci:
    nazwisko = student.split()[-1] 
    if nazwisko.startswith('N'):
        liczba_n += 1

print("Liczba studentow na N wynosi:", liczba_n)