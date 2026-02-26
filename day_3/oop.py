# Object Oriented Programming
# Concept used to structure code into
# reusable and modular components, in
# addition to data structures.

#  Class
# template for creating objects.
# specifies the attribute (data) and methods (functions)
# that a class's objects can have.
# defined using the class keyword
# objects are created using the class constructor

# class Student:
#     def __init__(self, stud_name, qual, age):
#         self.stud_name = stud_name
#         self.qual = qual
#         self.age = age

# student = Student("Tity Junior","Applications Development",26)

# print(student.stud_name)
# print(student.age)


# Inheritance
#  technique for creating a new class from an existing one
#  New class known as subclass, inherits data and functions of the superclass
#  Subclasses can extend or override the superclass's data and functions to create
#  new functionality.

# class Career(Student):
#     def __init__(self, stud_name, qual,age,choice_1, choice_2):
#         super().__init__(stud_name,qual, age)
#         self.choice_1 = choice_1
#         self.choice_2 = choice_2

# path = Career("Tity Junior","Applications Development",26, "Cloud Engineer","DevOps Engineer")

# print(path.stud_name)
# print(path.age)
# print(path.choice_1)
# print()
# print(path.choice_2)
#  Note positional args


# Polymorphism
# refers to the ability of objects to take on different forms or behaviours
# depending on their context.
# can be achieved by using inheritance and method overriding.
# as well as abstract classes and interfaces.

class Person:
    def __init__(self, name, country):
        self.name = name
        self.country = country
    def speak(self):
        print("My name is {} and I am from {}".format(self.name, self.country))


class Student(Person):
    def __init__(self, name, country, study):
        super().__init__(name, country)
        self.study = study
    def speak(self):
        print("Hi, I am {}, and I am from {}, currently studing {}.".format(self.name,self.country,self.study))


person = Person("Tity Junior","South Africa")
student = Student("Tity Junior","Durban","Python")

person.speak()
student.speak()