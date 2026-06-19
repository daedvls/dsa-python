"""Types of inheritance:
1. Single Inheritance"""

class A:
    def printA(self):
        print("This was printed from class A")

class B(A):
    def printB(self):
        print("This was printed from class B")

a = A()
b = B()

b.printA()  # This will call the method from class A (inherited)
b.printB()  # This will call the method from class B



"""
2. Multiple Inheritance
"""
class C:
    def printC(self):
        print("This was printed from class C")

class B(A, C):
    def printB(self):
        print("This was printed from class B")

# this is multiple inheritance
# class B inherits from multiple parent classes (A and C)

"""
3. Multilevel Inheritance
"""

class Alpha:
    def printAlpha(self):
        print("This was printed from class Alpha")

class Bravo(Alpha):
    def printBravo(self):
        print("This was printed from class Bravo")

class Charlie(Bravo):
    def printCharlie(self):
        print("This was printed from class Charlie")

# Bravo inherits from Alpha, and Charlie inherits from Bravo, forming a multilevel inheritance chain.


