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
#pseudokod
#l.pop
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

#drugipseudokod
print("-----------------------------------------------------------------------------------------")










