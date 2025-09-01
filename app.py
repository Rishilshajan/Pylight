# Basic code
#print("Hello World")
#print("50 + 10")
#print(50)
#print('A')

# To draw shapes
#print("   /|")
#print("  / |") 
#print(" /  |")
#print("/___|")
 
# Variables and data types
#a = 12
#b = 13 
#city = "London"
#print(a+b) 
#print(city)
#character_name = "Jo"
#character_age = "25"
#print("There once was a man named " + character_name + ",")
#character_age = "50" 
#print("He was " + character_age + " years old.")
#print(character_name +" was a good person.")
#d = 5.45678
#print(d)
#is_Male = True 
#print(is_Male)
#me = input()
#print(me + " World")
#a = "4"
#print(a)
#print(type(a)) 

#z = int(a)
#print(z)
#print(type(z))
#b = 2
#c = a/b
#print(c)
#print(type(c))
#height = int(input())
#print(height)
#print(type(height))

#Working with Strings
#print("Lion \ Academy")
#print("Lion \" Academy")
#print("Lion \nAcademy")
#phrase = "Lion Academy"
#print(phrase + " is cool")
#phrase = "Lion Academy"
#print(phrase.lower())
#print(phrase.upper())
#print(phrase.capitalize())
#print(phrase.title())
#print(phrase.islower())
#print(phrase.isupper())
#print(phrase.istitle())
#print(phrase.lower().islower())
#print(len(phrase))
#print(phrase[0])
#print(phrase[10])
#print(phrase.index("L"))
#msg = input()
#print(phrase.replace("Lion",msg))
#print(phrase.replace("Lion","Cat"))

#Working with Numbers
#print(450)
#print(450.00)
#print(-123)
#print(3 + 4.5)
#print(3 - 4.5)
#print(3 * 4.5)
#print(3 / 4.5)
#print(3 * 4 + 5)
#print(3 * (4 + 5))
#b = 20
#print(b % a)
#a = -10
#print(str(a) + " is my fav number")
#print(abs(a))
#print(pow(3, 3))
#print(max(45, 54))
#print(min(45,54))
#print(round(3.4))
#print(round(3.5))
#from math import *
#print(floor(3.7))
#print(ceil(3.7))
#print(sqrt(36))

#Getting Input from Users
#print("Enter the even number: ")
#a = input()
#print(a)
#name = input("Enter your name: ")
#age = input("Enter your age: ")
#print("Hello " + name +"!Your are " + age)

#Basic Calculator
#a = input("Enter you first number:")
#b = input("Enter you second number:")
#result =float(a)+ float(b)
#print(result)

#Mad Libs Game
#color = input("Enter a color: ")
#plural_noun = input("Enter a plural noun: ")
#celebrity = input("Enter a celebrity: ")
#print("Roses are " +color)
#print(plural_noun + " are Blue")
#print("I love " + celebrity)

#List is a versatile, ordered, and mutable collection of items
#friends = ["Sam","Kevin","Ryan",2,False]
#print(friends)
#friends[3] = "Maria"  
#print(friends[0])
#print(friends[-1:])
#print(friends[1:]) 
#print(friends[1:3])
#print(friends)

#List Functions
#lucky_num = [100000,4,8,12,14,26]
#friends = ["Sam","Kevin","Ryan","Don", "Amal","Shar","Don"]
#friends.extend(lucky_num)
#friends.append("Creed")
#print(friends)
#friends.insert(1,"Kelly")
#print(friends)
#friends.remove("Sam")
#print(friends)
#friends.clear()
#print(friends)
#friends.pop()
#print(friends)
#print(friends.index("Kevin"))
#print(friends.index("Shar"))
#print(friends.count("Don"))
#friends.sort()
#print(friends)
#lucky_num.sort()
#print(lucky_num)
#friends.reverse()
#print(friends)
#friends1 = friends.copy()
#print(friends1)
# To create a list from scratch in a shortcut method is List Comprehension
# variable = [expression for item in iterable] ; iterable can be range() or if conditionals
#num = [x for x in range(10)]
#print(num)
#nu = [x + 2 for x in range(5)]
#print(nu)
#group = [x for x in friends if x[0] != 'A']
#print(group)

#A Tuple in Python is an ordered and immutable collection data type, designed to store a fixed sequence of items.
#coordinates = (4,5,6,7,8,4,5,3)
#print(coordinates)
#print(coordinates.count(4))
#print(len(coordinates))
#latitude, *rest = coordinates   # *operator is used to split and group a tuple which is left behind.
#print(latitude)                 #*rest is the "starred expression" or "unpacking operator."  
#print(*rest)                    #It collects all the remaining elements from the coordinates tuple into a new list named rest
#print(coordinates[0])         
#coordinates[1] = 
#coord = [(1,2), (2,3)]
#print(coord)
#coord.append((4,5))
#print(coord)
#coord.remove((4,5))   
#print(coord)

#Functions
#def say_hi():
 #   name = input("Enter the name: ")
  #  print("Hello User")
   # print("Hello "+ name) 
#say_hi()
#print("Welcome to python")       
#def say_hi(name,age):
 #   print("Hello "+ name)
  #  print("You are "+ str(age) + " years old")
#say_hi("Amy",21)
#say_hi("Mike",22)
#say_hi("Steph",24)

#Return Statements
#def cube(num):
     #print("HI")
     #return num*num*num
#result = cube(4)
#print(result)    

#If Statement
#is_male = False
#is_tall = True
#if is_male or is_tall:
 #     print("You are a male and also tall or both")    
#else:
 #     print("You are neither male nor tall ")
#if is_male and is_tall:
 #     print("You are a tall male") 
#elif is_male and not(is_tall):
#      print("You are a short male")   
#elif not(is_male) and is_tall:
#      print("You are not a male but are tall")           
#else:
#      print("You are not a male and not tall ")   

#If Statements and Comparisions
#def max_num(num1,num2,num3):
 #  if num1 >= num2 and num1 >= num3:
 #   return num1
 #elif num2 >= num1 and num2 >= num3:
  #    return num2
   #else:
    #  return num3
#print(max_num(30,4,5)) 
#print("Maximum number is " + str(max_num(30,4,5)) )  

#Advanced Calculator
#num1 = float(input("Enter the first number: "))  
#num2 = float(input("Enter the second number: "))
#print("The operations are +, -, *, /")
#op = input("Enter the operation: ")
#if op == "+":
   # print(num1 + num2)
#elif op == "-":
    #print(num1 - num2)
#elif op == "*":
    #print(num1 * num2)
#elif op == "/":
    #print(num1 / num2)
#else:
    #print("Invalid operation")

#Sets - Unordered Collections; Does not suppport Indexing or Slicing; Mutable; Unique Values
#guests = {"Mary","Anna","John","Hai"}
#set1 = {"Hai","Hello","Anna",}
#print(guests)
#guests.add("Nate")
#guests.remove("Mary")
#print(guests)
#guests.clear()
#print(guests)
#comb = guests.union(set1)
#print(comb)
#com = guests.difference(set1)
#print(com)

#Dictionaries - A dictionary in Python is a mutable, ordered collection data type that stores data in key-value pairs.(From 3.7 versions of Python, it is ordered)
'''monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}
print(monthConversions["Mar"])
print(monthConversions.get("Dec"))
#me = str(input("Enter the first 3 letters of the month: "))
#print(monthConversions.get(me,"Not a valid key"))
info_keys = monthConversions.keys()
print(info_keys)
#info_values = monthConversions.values()
#print(info_values)
#info = monthConversions.items()
#print(info)
#monthConversions.update({"Jul":"july"})
#print(monthConversions.get("Jul"))
monthConversions.pop("Jul")
print(info_keys)
print("Jul" in monthConversions)
'''

#While Loop
#i = 1
#while i <= 10:
#   print(i)
#   i += 1 #i=i+1
#print("End of loop")   

#Match Case - Similiar to Switch Cases in other programming languages
# day = int(input("Enter a day: ")) 
# match day:
#   case 1:
#     print("Monday")
#   case 2:
#     print("Tuesday")
#   case 3:
#     print("Wednesday")
#   case 4:
#     print("Thursday")
#   case 5:
#     print("Friday")
#   case 6:
#     print("Saturday")
#   case 7:
#     print("Sunday")
#   case _:                 # "_" is the default case 
#     print("Enter a day between 1 and 7")  
#For combining cases we can use "|"
# day = 4
# match day:
#   case 1 | 2 | 3 | 4 | 5:
#     print("Today is a weekday")
#   case 6 | 7:
#     print("I love weekends!")


#BUilding a Guessing Game
#secret_word = 'giraffe'
#guess = ''
#guess_count = 0
#guess_limit = 3
#out_of_guesses = False
#while guess != secret_word and not(out_of_guesses):
 #   if guess_count < guess_limit:
 #       guess = input("Enter guess: ")
 #       guess_count += 1
 #   else:
 #       out_of_guesses = True
#if out_of_guesses:
#     print("Out of Guesses, YOU LOSE!")
#else:
#    print("You Win")               

#For Loop
#for i in range(10):
#    print(i)
#print("Done with the loop") 
#for letter in "Giraffe Academy":
 #   print(letter)
#friends = ["Jim","karen","Kevin"] 
#for name in friends:
 #   print(name)
#for i in range(len(friends)):
 #   print(friends[i])   
#for i in range(5):
#    if i == 0:
#        print("First Iteration")
#    elif i == 1:
#        print("Second Iteration")
#    else:
#        print("Not First Iteration")

#Exponent Function
# print(2**3)
#def raise_to_power(base_num, pow_num):
#    result = 1.0
#    for count in range(pow_num):
#        result *= base_num
#    return result
#a = float(input("Enter the base num: "))
#b = int(input("Enter the power num: "))
#print("The result is " + str(raise_to_power(a, b)))

#2D lists and Nested loops
#number_grid = [
 #   [1, 2, 3],
  #  [4, 5, 6],
   # [7, 8, 9],
   # [0] 
#]
#print(number_grid[0])
#print(number_grid[0][0])
#print(number_grid[2][1])
#for row in number_grid:
 #   for column in row:
  #      print(column)

#Build a translator
#vowels -> g
'''
def translate(phrase):  
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                  translation = translation + "G"
            else:
                  translation = translation + "g"
        else:
            translation = translation + letter
    return translation
print(translate(input("Enter a phrase: ")))            
'''
#Comments
'''
Hello
'''

#Try Except
#SyntaxError - Incorrect Syntax => print("Hello)
#NameError - Unknown Variable => name = "Anna" print(Surname)
#IndexError - Indexing out of range => student = ["Anna","Bob"] print(student[10])
#TypeError - Inappropriate Type => len(5)
#ValueError - Inappropriate Value => int("Hello")
#finally will print surely if exception occure or not
#else will print only if there are no exceptions in try block
#Custom Exceptions are given by raise   
#try:
   #value = 10/0
   #number = int(input("Enter a number: "))
   #print(number)
#except ZeroDivisionError:
#    print("Divided by zero")    
#except ValueError:
#    print("Invalid Input")  
#except ZeroDivisionError as err:
#    print(err)   
#finally:
#    print("Save") 
#product = ["ball","toy"] 
#try:
#    choice = product[1]
#except:
#    print("Error")   
#else:
#    print(choice + " is selected") 
#rate = 15
#if rate > 10:
#    raise ValueError("Enter below 10")          

   
#Reading Files
#r - read, w - write, r+ - read and write, a - append 
#employee_file = open("employ.txt","r") 
#print(employee_file.readable())
#print(employee_file.read())
#print(employee_file.readline())
#print(employee_file.readline())
#print(employee_file.readline())
#print(employee_file.readlines())
#print(employee_file.readlines()[2])
#for employ in employee_file.readlines():
 #   print(employ)
#employee_file.close()      

#Writing to Files:
#employee_file = open("employ.txt","a")
#employee_file.write("\nToby - Human Resources")
#employee_file.write("\nKelly - Customer Service")
#employee_file.close() 
#employee_file = open("employ.txt","w")
#employee_file.write("\nKelly - Customer Service")
#employee_file.close()
#employee_file = open("index.html","w")
#employee_file.write("<p>This is HTML</p>")
#employee_file.close()


#Modules and Pip
#import useful_tool
#print(useful_tool.roll_dice(10))


#Classes and Objects
#from student import Student
#student1 = Student("Jim", "Business", 3.1, False)
#print(student1.name)
#print(student1.major)
#print(student1.gpa)
#student2 = Student("Kelly", "Honors", 4.55, True)
#print( "\n" + str(student2.is_on_probation))

#Class Functions
#from student import Student
#student1 = Student("Jim", "Business", 3.1, False)
#student2 = Student("Kelly", "Honors",9.0, True)
#print(student1.on_honor_roll())
#print(student2.on_honor_roll())
#print(student1)
 

#Building A Mutilple Choice Quiz
'''
question_prompts = [
    "What color are apples?\n (a)Red/Green \n(b)Purple\n(c)Orange\n",
    "What color are bananas?\n (a)Teal\n(b)Magenta\n(c)Yellow\n",
    "What color are strawberries?\n (a)Yellow\n(b)Red\n(c)Blue\n",
    "What color are watermelons?\n (a)Red\n(b)Green\n(c)Pink\n",
]    
from Question import Question
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "a"),
]
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")
run_test(questions)
'''

#Inheritance
#from Chef import Chef
#from ChineeseChef import ChineeseChef
#myChef = Chef()
#myChef.make_special_dish()
#myChef.make_chicken()
#myChineeseChef = ChineeseChef()
#myChineeseChef.make_special_dish()

# Functional Programming (Intermediate)
   #Functions can be assigned to other variables and that variables can call that function body
#def welcome(name):
#    return "Welcome " + name
#greet = welcome
#print(greet("John"))
   #Higher Order Function - A function as an argument for another function
#def book_title(title):
#    return "Book Title: " + title
#def book(title,func):
#    return book_title(title)
#print(book("Bazooka",book_title))
   #Pure Function - A function giving same result for same input
#def total(price,count):
#    return price * count
#print(total(2,4)) 
   #Lambda Functions(Anonymous) -Functions without a name on a single line easy to use and create for a simple task 
#greet = lambda name: "Welcome " + name
#print(greet("John"))   
   #map function - Applies a specified function on every element in an iterable
   #filter function - Returns result based on a specific condition
#score = [85,50,34]
#def is_passing(score):
#    return score >= 55
#status = list(map(is_passing,score))   
#print(status)  
#a = list(filter( lambda score: score> 80, score))
#print(a)
   # *args - Any no. of arguments without creating a list before calling a function each time / Receives as Tuple
   # **kwargs - Recives in the form of dictionary as key value pair
   # def function_name(normal arguments, *args, **kwargs)
#def total(*args):
#    result = 0
#    for i in args:  
#        result += i
#    return result
#print(total(1,2,3,4,5,66,7))  
#def tot(**kwargs):
#    for i, j in kwargs.items():  
#        print(i, ":", j)
#tot(name="Alice", age=12) 
   #Decorators - A function(1) displaying a message. This message is taken by another function(2) as argument and performs an operation. This function(2) is called Decorators.
#def uppercase(func):  # Fixed function name
#    def wrapper():
#        print("Lights On")  # Fixed print statement
#        msg = func()
#        return msg.upper()  # Convert message to uppercase
#    return wrapper
#@uppercase  # Fixed decorator name
#def greet():
#    return "hello, world"
#print(greet())  # Calling the decorated function

#OOP - Object Oriented Programming - Polymorphism, Abstraction, Inheritance
#Blueprint = Class - Abstraction of Car
#Instances = Oject - A Green car
#To add attributes to a class
#Defining functions inside a class is called Methods
# class Car:
#     def __init__(self,brand,color):
#         self.brand = brand
#         self.color = color
#     def honk(self):
#         print("Beeep")    
# myCar = Car("Audi","Q5")
# print(myCar.color)  
# print(myCar.honk()) 
# For More details refer ChineeseChef.py 


#Python Interpreter
'''
Python is an interpreted language, which means that the source code is executed line by line. 
This is in contrast to a compiled language, where the source code is converted to machine code all at once.

Python is a dynamically typed language, which means that the type of a variable is determined at runtime. 
This is in contrast to a statically typed language, where the type of a variable is determined at compile time. 

Python is also an object-oriented language, which means that it supports the creation of objects with attributes and methods.
This is in contrast to a procedural language, where the focus is on the execution of procedures.

Python is also a high-level language, which means that it is designed to be easy to read and write. 
This is in contrast to low-level languages, which are designed to be close to the hardware and are more difficult to read and write. 

Python is also a general-purpose language, which means that it can be used for a wide variety of tasks. 
This is in contrast to a specialized language, which is designed for one specific task. 

Python is also a scripting language, which means that it is designed to be used interactively.
This is in contrast to a compiled language, where the source code is compiled into machine code all at once.
'''


#Detect Prime Numbers

# class Solution:
#     def listPrimes(self, n: int):
#         if n <= 2:
#             return 'No prime Number'  # Return an empty list if there are no primes

#         # Create a boolean list to keep track of prime numbers
#         is_prime = [True] * n
#         is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes

#         # Sieve of Eratosthenes
#         for i in range(2, int(n**0.5) + 1):
#             if is_prime[i]:
#                 for j in range(i * i, n, i): 
#                     is_prime[j] = False
        
#         # Collect and return the list of prime numbers
#         primes = [i for i, prime in enumerate(is_prime) if prime]
#         return primes

# # Example usage
# n = 89
# solution = Solution()
# print(solution.listPrimes(n))

