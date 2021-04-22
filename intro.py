# New member introduction to Python (April 2021)

# Variables are used to store data
# Some basic types of data we can store in variables:

# Numbers
# Integers vs Floats
number_of_students = 30
gallons_of_water = 4.15

# Strings: Sequence of characters. Single and double quotes.
greeting = "Hello"
name = 'Jack'


# We can easily display the value of a variable using the print() function
print(greeting)
print(number_of_students)

# We can interpolate variables of other data types into strings as well
print(f"There are {number_of_students} students present today.")

# We can use plus signs (+) to add strings together.
print(greeting + " " + name)

# We can also use operators to do some math
print(1 + 1)
print(5 - 1)
print(2 * 3)
print(10 / 2)
print(10 // 2) # Division that cuts off decimals
print(8 % 4) # Modular arithmetic (Returns the remainder of the division of a by b)
print(2 ** 3) # Power
print(gallons_of_water / number_of_students)

# We can also use operators to perform comparisons
print(10 > 2)
print(4 < 3)
print(5 <= 5)
print(9 >= 1)
print(8 == 6)
print(9 != 2)



# More comprehensive python guide:
# https://python.swaroopch.com

# Some neat sites for practice
# https://codingbat.com/python
# https://www.codeabbey.com/ 
# https://projecteuler.net/about (very math intensive, yet very rewarding)
