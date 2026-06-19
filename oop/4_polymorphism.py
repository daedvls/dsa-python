# Two things that look similar, but actually not similar

"""
Types of polymorphism:
1. Overloading: same function name, different signatures
2. Overriding: same function name, same signature


Note: Python doesn't support function overloading, but we can achieve it using default arguments or variable-length arguments.
traditionally, function overloading is achieved by defining multiple functions with the same name but different parameter lists.
However, in Python, if you define multiple functions with the same name, the last definition will overwrite the previous ones.



"""

# Overriding

class A:
    def print(self):
        print("a")

class B(A):
    def print(self):
        print("b")


b = B()
b.print() # Output: b
# Here, the print method in class B overrides the print method in class A. This is an example of method overriding,
# which is a form of polymorphism.
# The most recent definition of the method is the one that gets called.