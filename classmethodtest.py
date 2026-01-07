#Zugriff auf Klassenvariblen:
#============================

class Student:
    school_name = "Uni Wien"  # Klassenvariable
    
    @classmethod
    def get_school(cls):
        return f"School: {cls.school_name}"
    
    @classmethod
    def set_school(cls, name):
        cls.school_name = name

print(Student.get_school())  # School: Uni Wien
Student.set_school("TU Wien")
print(Student.get_school())  # School: TU Wien

#alternativer Konstruktor
#========================

from datetime import date

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"{self.name}'s age is: {self.age}")
    
    @classmethod
    def fromBirthYear(cls, name: str, birthYear: int):
        age = date.today().year - birthYear
        return cls(name, age)  # cls erlaubt Subklassen-Erweiterung!
        #return Person(name,age)

# Normaler Konstruktor
p1 = Person("Max", 30)
p1.display()  # Max's age is: 30

# Alternativer Konstruktor
p2 = Person.fromBirthYear("Anna", 1990)
p2.display()  # Anna's age is: 36


