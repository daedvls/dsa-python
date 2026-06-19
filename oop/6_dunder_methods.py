# aka Magic Methods

"""
1. __init__()

2. __str__()

3. __add__(), __sub__(), __mul__(), __truediv__(), __floordiv__(), __mod__(), __pow__()

4. __len__()
"""


class a:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return f"this is a class with x = {self.x}"  # basically its like a print function for the class

    def __add__(self, other):
        return self.x + other.x

    def __len__(self):
        return 10 # or sth else in a more complex case

temp = a(5)
print(temp)     # This will print whatever is in __str__ method
# If we don't have __str__ method, it will print the object location in memory (e.g., <__main__.a object at 0x7f8c2c3d1d30>)


temp2 = a(10)
print(temp + temp2)  # This will call the __add__ method and return the sum of x values
# Essentially, __add__ method is called when we use the + operator between two objects of class a

print(len(temp))  # This will call the __len__ method and return 10


