class MyComplex():
    
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def add(self,other):
        re=self.re+other.re
        im=self.im+other.im
        return MyComplex(re, im)

    def __add__(self,other):
        return self.add(other)

    def __repr__(self):
        return f"{self.re}+{self.im}i"

c1 = MyComplex(1, 2)
c2 = MyComplex(3, 4)
print(c1)
print(c2)

c3=c1.add(c2)
print(c3)
print(c1+c2)