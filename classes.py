# class Myclass:
#     def __init__(self, name, age, i):
#         self.name = name
#         self.age = age
#         self.i=i
 
#     def display(self):
#         for _ in range(self.i):
#             print("Name:", self.name)
#             print("Age:", self.age)

# Obj1=Myclass("Samrat", 27)
# Obj1.display()

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)

class Animal:
    def breathe(self):
        print("Breathing...")

# Child Class (Inherits from Animal)
class Cat(Animal):
    def purr(self):
        print("Purring...")

my_cat = Cat()
my_cat.breathe()  # Inherited from Animal
my_cat.purr()
