## see my book notes

# count = 0
# name = str(input("What is your name?"))

# while count < 5:
#     print(name, "is awesome!")
#     count += 1

# for i in range(5, 11):
#         print(i)

#qa exercise
# name = ["cr7", "Messi", "neymar", "giggs", "pirlo"]
# i = 0
# while i < len(name):
#   print(name[i])
#   i = i + 1

# 1. Write a Python program to find those numbers 
# which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)
# found = []
# for numbers in range(1501, 27001):
#     if (numbers %7 == 0) and (numbers %5 == 0):
#         # print(numbers)
#         (found.append(numbers))
# print(found)        


# 2. Write a Python program to convert temperatures to and from celsius, fahrenheit. Go to the editor
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
# Expected Output :
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius

# ## nest loops
# for i in range(3):
#     for j in range(4):
#         print(i, "x", j, "=", i * j)

# Functions
# def greet(firstname, lastname):
#     return f"Hello {firstname} {lastname}"

# print(greet("Steve", "Rogers"))

# def greet(name):
#     return f"Hello {name}"

# name = input("What is your name? ")   ###avoided using print() etc.. inside function so we can reuse whenever
# print(greet(name))

####Default Values and Keyword Arguments
# If we want to allow for flexibility in our function, we could make use of default values that are assigned
#  to parameters when arguments are not specified. e.g
# def greet(name, greeting="Hello"):
#     return f"{greeting} {name}"
# print(greet("Steve"))  # Prints "Hello Steve"
# print(greet("Bill", "Hola"))  # Prints "Hola Bill"

### tutorial
def add_calc(number1, number2):
    answer = number1 + number2
    return answer

added_number = add_calc(5,5)
print(added_number + 20)
# The output will be 30.

#FUNCTIONS EXCERCISE
# def determine_grade(scores):
#     if scores >= 90:
#         return 'A'
#     elif scores >= 80:
#         return 'B'
#     elif scores >= 70:
#         return 'C'
#     elif scores >= 60:
#         return 'D'
#     elif scores >= 50:
#         return 'E'
#     else:
#         return 'F'

# grade = determine_grade(int(input("What was your score?")))
# print(f"your grade was: {grade}")



##Modules

# import math    ##import math module

# number = float(input("Enter a number: ")) 
# answer = math.sqrt(number) #using its sqrt function to find the square root of the entered number
# print(answer)

# import math
# import random

# def random_pi():
#     return math.ceil(random.randint(1, 10) * math.pi)

# for _ in range(5):
#     print(random_pi())

# Importing Objects From Modules
# from math import pi, floor
# from random import randint

# def random_pi():
#     return ceil(randint(1, 10) * pi)

# for _ in range(5):
#     print(random_pi())

    

    