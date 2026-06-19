# Designing a complex number class/object in python

class complexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return complexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return complexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return complexNumber(real_part, imag_part)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

    def __abs__(self):
        return (self.real**2 + self.imag**2)**0.5