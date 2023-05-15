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