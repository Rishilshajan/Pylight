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

#Lists Mutable
#friends = ["Sam","Kevin","Ryan",2,False]
#print(friends)
#friends[3] = "Maria"  
#print(friends[0])
#print(friends[-1])
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

#Tuples Immutable
#coordinates = (4,5)
#print(coordinates)
#coordinates[1] = 3
#print(coordinates[0])
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
#say_hi("Amina",21)
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

#Dictionaries
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
me = str(input("Enter the first 3 letters of the month: "))
print(monthConversions.get(me,"Not a valid key"))
'''
#While Loop
#i = 1
#while i <= 10:
#   print(i)
#   i += 1 #i=i+1
#print("End of loop")    

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
#print("bewicfjbec")

#Try Except
#try:
#   value = 10/0
#   number = int(input("Enter a number: "))
#   print(number)
#except ZeroDivisionError:
 #   print("Divided by zero")    
#except ValueError:
 #   print("Invalid Input")  
#except ZeroDivisionError as err:
 #   print(err)   
   
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
#employee_file = open("employ1.txt","w")
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

#Python Interpreter
#Python is an interpreted language, which means that the source code is executed line by line. This
#is in contrast to a compiled language, where the source code is converted to machine code all at
#once. Python is a dynamically typed language, which means that the type of a variable is determined
#at runtime. This is in contrast to a statically typed language, where the type of a variable
#is determined at compile time. Python is also an object-oriented language, which means that it
#supports the creation of objects with attributes and methods. This is in contrast to a procedural
#language, where the focus is on the execution of procedures. Python is also a high-level language
#, which means that it is designed to be easy to read and write. This is in contrast to
#low-level languages, which are designed to be close to the hardware and are more difficult to read
#and write. Python is also a general-purpose language, which means that it can be used for
#a wide variety of tasks. This is in contrast to a specialized language, which is designed for
#one specific task. Python is also a scripting language, which means that it is designed to be
#used interactively. This is in contrast to a compiled language, where the source code is
#compiled into machine code all at once. Python is also a dynamically typed language, which means that
#the type of a variable is determined at runtime. This is in contrast to a statically typed language
#, where the type of a variable is determined at compile time. Python is also an object-oriented
#language, which means that it supports the creation of objects with attributes and methods. This is in
#contrast to a procedural language, where the focus is on the execution of procedures. Python is also
#a high-level language, which means that it is designed to be easy to read and write. This
#is in contrast to low-level languages, which are designed to be close to the hardware and are
#more difficult to read and write. Python is also a general-purpose language, which means that it
#can be used for a wide variety of tasks. This is in contrast to a specialized language,
#which is designed for one specific task. Python is also a scripting language, which means that it
#is designed to be used interactively. This is in contrast to a compiled language, where the
#source code is compiled into machine code all at once. Python is also a dynamically typed language,
'''
class Solution:
    def listPrimes(self, n: int):
        if n <= 2:
            return 'No prime Number'  # Return an empty list if there are no primes

        # Create a boolean list to keep track of prime numbers
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes

        # Sieve of Eratosthenes
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False
        
        # Collect and return the list of prime numbers
        primes = [i for i, prime in enumerate(is_prime) if prime]
        return primes

# Example usage
n = 2
solution = Solution()
print(solution.listPrimes(n))
'''
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head 
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_with_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next and current_node.next.data != data:
            current_node = current_node.next
        if current_node.next:
            current_node.next = current_node.next.next

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' -> ')
            current_node = current_node.next
        print('None')

# Creating a linked list and performing operations
ll = LinkedList()

# Appending elements
ll.append(1)
ll.append(2)
ll.append(3)

# Prepending an element
ll.prepend(0)

# Printing the linked list
ll.print_list()  # Output: 0 -> 1 -> 2 -> 3 -> None

# Deleting an element
ll.delete_with_value(2)

# Printing the linked list again
ll.print_list()  # Output: 0 -> 1 -> 3 -> None
'''
class Stack():
    def __init__(self):
        self.my_stack = []
        self.head = -1
        self.opr_limit = 100
        self.bottow_el = None
        self.size = 0
        
    def stack(self, val):
        self.my_stack.append(val)
        self.head += 1
        self.size += 1
        if self.head == 0:
            self.bottow_el = val
            
    def unstack(self):
        val = self.my_stack[self.head]
        del self.my_stack[self.head]
        self.head -= 1
        self.size -= 1
        if self.head < 0:
            self.bottow_el = None
        
        return val
        
    def get_bottow(self):
        return self.bottow_el
        
    def get_top(self):
        return self.my_stack[self.head]
        
    def tostr(self):
        return (self.my_stack)
        
n_queries = int(input())
stack_1 = Stack()
stack_2 = Stack()

for e in range(n_queries):
    query_s = str(input()).split()
    
    if query_s[0] == "1":
        stack_1.stack(int(query_s[1]))
        
    elif query_s[0] == "2":
        if stack_2.size > 0:
            stack_2.unstack()
        else:
            for e in range(stack_1.size):
                stack_2.stack(stack_1.unstack())
            stack_2.unstack()
    else:
        if stack_2.size > 0:
            print(stack_2.get_top())
            
        else:
            print(stack_1.get_bottow())    
i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print(0)   
    