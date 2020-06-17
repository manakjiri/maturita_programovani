""" 
Charakteristika OOP, třída (atribut, metoda), instance – stejné rozhraní, ale jiné atributy

Dědičnost, polymorfismus, zapouzdření
Třída – class, konstruktor __init__(self)
"""

# dedicnost, super() odkazuje na materskou class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)
    
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

guy = Student('John', 'Smith', 2020)
guy.welcome()
