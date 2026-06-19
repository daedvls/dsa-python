"""

- Access specifiers: controls visibility of class members.
three types: Public, Protected, Private

Public: available for access to all
Protected: Available for access to class and its children
Private: Available for access to class only


Protected data members are denoted by a single underscore prefix (e.g., _password).
Private data members are denoted by a double underscore prefix (e.g., __balance).


ENCAPSULATION


Encapsulation means:
    Bundling data and methods together
    while restricting direct access.

Python doesn't have strict private members
like C++ or Java.

Instead:

    _variable      -> protected (convention)
    __variable     -> private (name mangling)

Double underscore is used to hide implementation details.
"""

# ex
class Student:
    name = ""
    age = 0
    location = ""
    __password = "123"  # this can't be accessed outside this class. Then how do we use it?
                        # we use getter and setter methods to access private variables


    @property
    def password(self):
        print("getter is called")
        return self.__password


    @password.setter
    def password(self, new_password):
        print("setter is called")
        self.__password = new_password


student1 = Student()
print(student1.password)  # getter is called, 123
student1.password = "456"  # setter is called
print(student1.password)  # getter is called, 456

