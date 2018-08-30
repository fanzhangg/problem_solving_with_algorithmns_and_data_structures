# encoding: utf-8
# module 1.13_fraction.py

# classes


class Fraction:
    """
        A class to implement the abstract data type fraction
    """
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __add__(self, other):
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        common = self.gcd(new_num, new_den)
        if new_num % new_den:
            return Fraction(new_num//common, new_den//common)
        else:
            return new_num // new_den

    def __sub__(self, other):
        new_num = self.num * other.den - self.den * other.num
        new_den = self.den * other.den
        common = self.gcd(new_num, new_den)
        if new_num % new_den:
            return Fraction(new_num//common, new_den//common)
        else:
            return new_num // new_den

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        common = self.gcd(new_num, new_den)
        if new_num % new_den:
            return Fraction(new_num//common, new_den//common)
        else:
            return new_num // new_den

    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        common = self.gcd(new_num, new_den)
        if new_num % new_den:
            return Fraction(new_num//common, new_den//common)
        else:
            return new_num // new_den

    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = self.den * other.num
        return first_num == second_num

    def __gt__(self, other):
        first_num = self.num * other.den
        second_num = self.den * other.num
        return first_num > second_num

    def __ge__(self, other):
        first_num = self.num * other.den
        second_num = self.den * other.num
        return first_num >= second_num

    def __lt__(self, other):
        first_num = self.num * other.den
        second_num = self.den * other.num
        return first_num < second_num

    def __le__(self, other):
        first_num = self.num * other.den
        second_num = self.den * other.num
        return first_num <= second_num

    @staticmethod
    def gcd(m, n):
        while m % n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm % oldn
        return n


if __name__ == "__main__":
    x = Fraction(5, 3)
    y = Fraction(6, 7)
    print(x + y)
    print(x * y)
    print(x / y)
    print(x > y)
    print(x >= y)
    print(x == y)
    print(x < y)
    print(x <= y)
