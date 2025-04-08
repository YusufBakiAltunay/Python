# Objectgeoriënteerd Programmeren (OOP)

#from car import Car

#car1 = Car("Mustang", 2025, "red", False)
#car2 = Car("Corvette", 2024, "yellow", False)
#car3 = Car("Charger", 2022, "blue", True)

#print(car2.model)
#car2.drive()


class Student:

    class_year = 2024

    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Patrick", 30)
student2 = Student("Alex", 25) 

print(student2.name)
print(student2.age)
print(student2.class_year)