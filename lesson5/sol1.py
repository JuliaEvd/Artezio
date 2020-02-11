from math import sqrt


class Complex:
    def __init__(self, x=0, y=0):
        self.re = x
        self.im = y

    def __add__(self, other):  # +
        return Complex(self.re + other.re, self.im + other.im)

    def __sub__(self, other):  # -
        return Complex(self.re - other.re, self.im - other.im)

    def __mul__(self, other):  # *
        return Complex(self.re * other.re - self.im * other.im,
                       self.re * other.im + self.im * other.re)

    def __truediv__(self, other):  # /
        return Complex((self.re * other.re + self.im * other.im)
                       / (other.re ** 2 + other.im ** 2),
                       (other.re * self.im - self.re * other.im)
                       / (other.re ** 2 + other.im ** 2))

    def __abs__(self):
        return Complex(sqrt(self.re ** 2 + self.im ** 2))

    def __str__(self):
        return "{0.real:.2f}{0.imag:+.2f}i".format(self.re, self.im)


c = Complex(2, 1)
d = Complex(5, 6)

print(c + d)
print(c - d)
print(c * d)
print(c / d)
print(abs(c))
print(abs(d))
