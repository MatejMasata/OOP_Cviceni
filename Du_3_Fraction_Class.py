from math import gcd

"""
    vvvv      YOUR SOLUTION      vvvv
"""


class Fraction:

    def __init__(self, num, den):
        # "constructor", more precisely "initializer"
        # initialize Fraction here
        self.num=num
        self.den=den

    def __repr__(self):
        # magic method for text representation
        # return Fraction as a string in `numerator/denominator` format, e.g 1/2, 3/4, 153/468 etc.
        return f"{self.num}/{self.den}"
        

    def normalize(self):
        # from this Fraction get normalized Fraction, return normalized Fraction
        g=gcd(self.num,self.den) # greatest common divisor
        num_nor=self.num//g
        den_nor=self.den//g
        return Fraction(num_nor, den_nor)
        

    def __eq__(self, other):
        # magic method for comparison `==`
        # compare two fractions if they are same
        # two Fractions are same if their normalized numerators and denominators are equal respectively
        # example 1/3 is equal to 2/6, 1/3 is not equal to 3/1
        self_nor=self.normalize()
        other_nor=other.normalize()
        if self_nor.num==other_nor.num and self_nor.den==other_nor.den:
            return True
        else:
            return False

    def __lt__(self, other):
        # magic method for comparison `<`
        # compare two fractions if the first one is less than second one
        # example 1/3 <= 1/2
        #common_den=self.normalize().den*other.normalize().den
        self_num=self.num*other.den
        other_num=other.num*self.den

        if self_num<other_num:
            return True
        else:
            return False

    def __le__(self, other):
        # magic method for comparison `<=`
        # compare two fractions if the first one is less than or equal to the second one
        # example 1/3 <= 1/2
        self_num=self.num*other.den
        other_num=other.num*self.den

        if self_num<=other_num:
            return True
        else:
            return False

    def add(self, other):
        # take other Fraction, execute adding, return new Fraction with the result
        num=self.num*other.den+other.num*self.den
        den=self.den*other.den
        return Fraction(num, den)

    def sub(self, other):
        # take other Fraction, execute subtraction, return new Fraction with the result
        num=self.num*other.den-other.num*self.den
        den=self.den*other.den
        return Fraction(num, den)

    def mul(self, other):
        # take other Fraction, execute multiplication, return new Fraction with the result
        num=self.num*other.num
        den=self.den*other.den
        return Fraction(num, den)

    def div(self, other):
        num=self.num*other.den
        den=self.den*other.num
        return Fraction(num, den)

    def __add__(self, other):
        # magic method for operation `+`
        # same as add()
        return self.add(other)

    def __sub__(self, other):
        # magic method for operation `-`
        # same as sub()
        return self.sub(other)

    def __mul__(self, other):
        # magic method for operation `*`
        # same as mul()
        return self.mul(other)

    def __truediv__(self, other):
        # magic method for operation `/`
        # same as div()
        return self.div(other)


"""
    ^^^^      YOUR SOLUTION      ^^^^
#################################################################
    vvvv TESTS FOR YOUR SOLUTION vvvv
"""


# constructor
assert Fraction(1, 2).num == 1 and Fraction(1, 2).den == 2

# repr
assert f"{Fraction(1, 2)}" == "1/2"

# normalization
assert Fraction(3, 6).normalize().num == 1 \
       and Fraction(3, 6).normalize().den == 2 \
       and type(Fraction(3, 6).normalize().num) is int \
       and type(Fraction(3, 6).normalize().den) is int

# comparison magic
assert Fraction(1, 3) == Fraction(2, 6)
assert not(Fraction(1, 3) == Fraction(3, 1))
assert Fraction(1, 3) <= Fraction(1, 2)
assert Fraction(1, 3) < Fraction(1, 2)


# operation methods
assert Fraction(1, 2).add(Fraction(1, 3)) == Fraction(5, 6)
assert Fraction(1, 2).sub(Fraction(1, 3)) == Fraction(1, 6)
assert Fraction(2, 2).mul(Fraction(1, 3)) == Fraction(1, 3)
assert Fraction(1, 2).div(Fraction(1, 3)) == Fraction(3, 2)


# operators magic
assert Fraction(1, 2) + Fraction(1, 3) == Fraction(5, 6)
assert Fraction(1, 2) - Fraction(1, 3) == Fraction(1, 6)
assert Fraction(1, 2) * Fraction(1, 3) == Fraction(1, 6)
assert Fraction(1, 2) / Fraction(1, 3) == Fraction(3, 2)
