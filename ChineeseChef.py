from Chef import Chef
class ChineeseChef(Chef): #Example of Child Class inheriting properties from Parent Class
    def make_special_dish(self):
        print("The Chef  makes Orange Chicken")
    def make_french_fries(self):
        print("The chef makes french fries")

#SuperClass/ Parentclass - The class from which properties are inherited
#Subclass/ Childclass - The class which inherits the properties
# If we want to inherit attributes from parent class and also add some attributes to child class use super().init() to inherit from parent class and init() in child class        
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# per = Person("John",23)
# print(per.name)
# class Student(Person):
#     def __init__(self,name,age,faculty):
#         super().__init__(name,age)
#         self.faculty = faculty
# stu = Student("John",23,"CS")   
# print(stu.faculty)     
#Method overriding - Method with same name but with different operations

#Data Hiding - Protect certain class attributes and methods
#First Level is (self._age = age) Underscore after dot notation
#Second Level is (self.__age = age) two Underscore after dot notation
#Protected Attribute - Accessible but use cautiously outside the class
#Private Attribute - Not Accessible ; Accessing inside within a class method enables Data Encapsulation ; Can be accessed if necessary using Name Mangling
# class Person:
#     def __init__(self,name,age):
#         self.__name = name  #Private Attribute
#         self._age = age  #Protected Attribute
# per = Person("John",23)
# print(per.name)

# Class demonstrating class methods, static methods, private and protected attributes
class Person:
    def __init__(self, name, age):
        self.__name = name  # Private Attribute (Cannot be accessed directly)
        self._age = age  # Protected Attribute (Can be accessed but should be treated as private)
    # Class Method: Works with the class itself, not instances
    @classmethod
    def show_info(cls, color):
        print("Class Method Called: Favorite Color is {color}")

    # Static Method: Does not access instance or class attributes
    @staticmethod
    def greet():
        print("Hello! This is a static method.")

    # Method to access private attribute
    def get_name(self):
        return self.__name
# Creating an instance of Person
per = Person("John", 23)

# Accessing a protected attribute (not recommended, but possible)
print("Accessing protected attribute _age:", per._age)

# Trying to access private attribute directly (will cause error)
# print(per.__name)  # Uncommenting this will raise an AttributeError

# Correct way to access private attribute using a method
print("Accessing private attribute __name using method:", per.get_name())

# Calling Class Method
Person.show_info("Green")  # Called on class itself

# Calling Static Method
Person.greet()  # No instance or class data required
  
    