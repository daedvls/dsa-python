class Student:

    # Class Variable
    # Shared by ALL objects of this class.
    school_name = "IITK"

    def __init__(self, name, roll_no, password):
        """
        CONSTRUCTOR

        __init__ is called automatically whenever an object
        is created.

        It initializes object attributes.

        self refers to the CURRENT object being created.
        """

        self.name = name
        self.roll_no = roll_no
        self.__password = password

    def introduce(self):
        """Instance Method"""

        print(
            f"Hi, I am {self.name} "
            f"and my roll number is {self.roll_no}"
        )

    @property
    def password(self):
        print("getter is called")
        return self.__password

    @password.setter
    def password(self, new_password):
        print("setter is called")
        if len(new_password) < 6:
            print("Password must be at least 6 characters long.")
            return
        self.__password = new_password




print("CONSTRUCTOR EXAMPLE")


# Creating objects
s1 = Student("Joel", 101)
s2 = Student("Alice", 102)

s1.introduce()
s2.introduce()

print("School:", Student.school_name)