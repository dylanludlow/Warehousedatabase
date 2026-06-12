#Declare one string, one floating-point, one boolean
#Print the variables
#Print types of the variables
# Declare one string, one floating-point, one boolean
from operator import add

name = "Dylan"
height = 1.75
is_student = True

# Print the variables
print(name)
print(height)
print(is_student)

# Print types of the variables
print(type(name))
print(type(height))
print(type(is_student))

#Declare 2 variables and use every math operator
a = 15
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)


#Check if the temperature is greater than 20 and less than 30
temperature = 26
print(temperature)
print(temperature < 30)
print(temperature > 20)

print(30 > temperature > 20)

print(temperature > 20 and temperature < 30)

#Check if number is odd or even

number = 10
reminder = number % 2
print("Number {} is even {}".format(number, reminder == 0))
print("Number {} is odd {}".format(number, reminder == 1))

#Tickets for the cinema
ticket_price = 35
minimum_age = 16


#Ask user about age, and how much money he/she have

age = int(input ("How old are you?"))
money = int(input ("How much money do you have?"))

result = age >= minimum_age and money >= ticket_price
print("You can watch the film {}".format(result))

