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
        print(repr(razlomak))
        
    def __sub__(self, other):
        brojnik1 = (self.brojnik * other.nazivnik) - (other.brojnik * self.nazivnik)
        nazivnik1 = self.nazivnik * other.nazivnik
        razlomak = Razlomak(brojnik1, nazivnik1)
        razlomak.skrati
        print(repr(razlomak))

    def __mul__(self, other):
        brojnik1 = self.brojnik * other.brojnik
        nazivnik1 = self.nazivnik * other.nazivnik
        razlomak = Razlomak(brojnik1, nazivnik1)
        razlomak.skrati
        print(repr(razlomak))

    def __truediv__(self, other):
        brojnik1 = self.brojnik / other.brojnik
        nazivnik1 = self.nazivnik / other.nazivnik
        razlomak = Razlomak(brojnik1, nazivnik1)
        razlomak.skrati
        print(repr(razlomak))

    


        
                
                

    
    
    
