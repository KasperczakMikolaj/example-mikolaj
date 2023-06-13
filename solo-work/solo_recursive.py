#   funkcja sum_list l 
#   is l empty?
#      y ->0
#      n -> 1[0] + reszta                               [_,_,_,_] -->  1+f[2,3]->6 --> 2+f[3]->5 --> 3+ f[]->3
#                      | 
#                      V
#                       sum_list(reszta) 
#                           return...
#           (lista1=[1,2,3]
#              print lista1

def lista(wybrana_lista):
    if len(wybrana_lista) == 0:
        return 0
    else:
        return wybrana_lista[0] + lista(wybrana_lista[1:])
mikolaj_lista = [1,2,3,4]
sum = lista(mikolaj_lista)
print(sum)
#funkcja lista sumuje rekurencyjnie wszystkie elementy danej listy, zaczynając od pierwszego elementu i dodając go do sumy reszty listy, aż do momentu, gdy lista jest pusta. Wynik sumy jest wypisywany na końcu.

print("-----------------------------------------------------------------------------------------")

def najwieksza_wartosc(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        jeden = lista[0]
        reszta = lista[1:]
        reszta = najwieksza_wartosc(reszta)
        if jeden > reszta:
            return jeden
        else:
            return reszta
        
moja_lista = [1,2,3]
max_element = najwieksza_wartosc(moja_lista)
print("Największa wartość z listy wynosi",  str(max_element))

 #funkcja rekurencyjnie dzieli listę na część pierwszą i resztę, a następnie znajduje największą wartość w reszcie listy. W końcu porównuje tę wartość z pierwszym elementem listy i zwraca większą wartość jako największą wartość w całej liście.

print("-----------------------------------------------------------------------------------------")

# Suma Listy
# is l empty ? 
#(yes) y -> 0
#(no) n -> l(0) + suma(reszta)

def sum_list(lista):
    if len(lista) == 0:    
        return 0           
    else:
        return lista[0] + sum_list(lista[1:])   

#lista_Mikolaj
lista_Mikolaj = [1,2,3,4,5]
sum = sum_list(lista_Mikolaj)
print(f"Wynik to:", sum)
print("---------------------------------------")

# Silnia
#Silnia(i)
# Czy i = 0     ?     
# (yes) y - 1 bo 0!=1
# (no)  y - i * silnia(i-1)

def Silnia(i):
    if i == 0:       
        return 1
    else:
        return i * Silnia(i-1)
licz= 5
wynik = Silnia(licz)
print(f"Silnia wynosi:", wynik)
print("----------------------")








