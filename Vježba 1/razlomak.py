#Zadatak 1.1
class Razlomak(object):

    def __init__(self, brojnik, nazivnik):
        self._brojnik = brojnik
        self._nazivnik = nazivnik

    @property
    def brojnik(self):
        return self._brojnik
    @brojnik.setter
    def brojnik(self, value):
        self._brojnik = value

    @property
    def nazivnik(self):
        return self._nazivnik
    @nazivnik.setter
    def nazivnik(self, value):
        self._nazivnik = value

    @property
    def skrati(self):
        djelitelj = 0

        if self.brojnik < self.nazivnik:
            manji = self.brojnik
        else:
            manji = self.nazivnik

        for i in range(2,int(manji+1)):
            if self.brojnik%i==0 and self.nazivnik%i==0:
                djelitelj = i

        if djelitelj == 0:
            print("Ne može se skratiti.")

        else:
            self.brojnik //= djelitelj
            self.nazivnik //= djelitelj

#Zadatak 1.2

    def __repr__(self):
        return "Razlomak(" + repr(self._brojnik) + ", " + repr(self._nazivnik) + ")"

    def __str__(self):
        return "Razlomak " + str(self._brojnik) + "|" + str(self._nazivnik)

    def __eq__(self, other):
        return (self.brojnik / self.nazivnik) == (other.brojnik / other.nazivnik)
    def __lt__(self, other):
        return (self.brojnik / self.nazivnik) < (other.brojnik / other.nazivnik)
    def __le__(self, other):
        return (self.brojnik / self.nazivnik) <= (other.brojnik / other.nazivnik)

#Zadatak 1.3

    def __add__(self, other):
        brojnik1 = (self.brojnik * other.nazivnik) + (other.brojnik * self.nazivnik)
        nazivnik1 = self.nazivnik * other.nazivnik
        razlomak = Razlomak(brojnik1, nazivnik1)
        razlomak.skrati
        return repr(razlomak)
        
    def __sub__(self, other):
        brojnik1 = (self.brojnik * other.nazivnik) - (other.brojnik * self.nazivnik)
        nazivnik1 = self.nazivnik * other.nazivnik
        razlomak = Razlomak(brojnik1, nazivnik1)
        razlomak.skrati
        return repr(razlomak)

    def __mul__(self, other):
        brojnik1 = self.brojnik * other.brojnik
        nazivnik1 = self.nazivnik * other.nazivnik
        razlomak = Razlomak(brojnik1, nazivnik1)
        razlomak.skrati
        return repr(razlomak)

    def __truediv__(self, other):
        brojnik1 = self.brojnik / other.brojnik
        nazivnik1 = self.nazivnik / other.nazivnik
        razlomak = Razlomak(brojnik1, nazivnik1)
        razlomak.skrati
        return repr(razlomak)
        
print('*** test 1 ***')
r1 = Razlomak(12, 30)
print(r1.brojnik, r1.nazivnik)
r1.skrati
print(r1.brojnik, r1.nazivnik)

print('*** test 2 ***')
r1 = Razlomak(12, 30)
r2 = Razlomak(2, 5)
r3 = Razlomak(3, 6)
print(r1, r2, repr(r3))
print(r1 == r2)
print(r3 >= r1)
print(r3 < r2)

print('*** test 3 ***')
print(Razlomak(8, 4) + Razlomak(5, 2))
print(Razlomak(9, 3) - Razlomak(2, 6))
print(Razlomak(2, 2) * Razlomak(4, 2))
print(Razlomak(12, 8) / Razlomak(30, 5))

    


        
                
                

    
    
    
