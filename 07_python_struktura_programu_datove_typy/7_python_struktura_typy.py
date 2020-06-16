""" 
Charakteristika: je to interpretovaný dynamický objektově orientovaný programovací jazyk
Interpretovaný znamená, že se nepřekládá do instrukcí procesoru rovnou (kompiluje), ale do bajtového kódu, který pak interpreter převádí na instrukce procesoru
Objektově orientovaný – využívá výhody objektů = dědičnost a polymorfismus
Dynamický – nemusíme definovat proměnné, proměnná se definuje její deklarací, tedy prvním použitím
Jednoduché datové typy – ukázka int, float, string
Příkaz type()
Funkce nad číselnými typy – round(), abs(), max(), min()
Modul math – math.trunc(), math.floor()
Nový soubor – program Papoušek, Faktoriál
"""

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

