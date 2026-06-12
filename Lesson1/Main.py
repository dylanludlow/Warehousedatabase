print("Hello World")
print("hello world")
#variable message
message = "Hello"
print(message)
print(message)
print(message)
print(message)

message = message + " world"
print(message)
print(message)
#integer number - without "dot"
counter = 2
print(counter)


#Floating-point number
weight_sum = 10.5
print(weight_sum)
#Boolean variable (True or False)
always_true = True
print(always_true)
always_false = False
print(always_false)

#Text variable (Strings)
message = 'Hello World'
print (message)
message = "Hello World"
print(message)

long_message = '''
Line 1
Line 2
hahashns
uwuiewuieuiewui
123123
4545
'''
print(long_message)

#None - nothing
nothing_here = None
print(nothing_here)

#Math operators
a = 1.5
b = 0.5
print(a + b)
print(a - b)
print(a * b)
print(a / b)

a = 2
b = 3
print(a ** b) #a to the power of b (2*2*2)
print(b % a) #Reminder from dividing
print(15 % 6) #15/6 -> 6 + 6 + 3


#Compairing variables
a = 1
b = 2
print(a == b) #Equals (double '==' !!!)
print(a != b) #Different
print(a < b) #Less
print(a > b) #Greater
print(a <= b) #Less or equal
print(a >= b) #Greater or equal

#Logical operators (Works only with logical variables - Booleans)
print(True and True)
print(True or False)
print(False and True)
print(False or False)
print(not True)
print(not False)

#Variabes in Boolean context

print(bool(-1)) #Ture
print(bool(1)) #True
print(bool(2)) #True
print(bool(0)) #False
print(bool(""))

#Checking variable type
a = "SomeText"
print(type(a))

print(type(a) is str)
print(type(a) is not str)

print(2 + 2)
print("2" + "2")

print(int("2") + int("2"))
print(str(2) + str(2))

#Text Operations
print("Hello" + " " + "World")
print("Hello" * 5)


str1 = "a"
int1 = 1

print("Text fot %s formatting %i" % (str1, int1)) #Deprecated
print("Text for {} formatting {}".format(str1, int1))
print(f"test for {str1} formatting {int1}")



#Getting user input
print("Whats your name?")
user_name = input()
print("Your name is {}".format(user_name))

print("How old are you?")
age = input() #String
print("Your age is {}".format (age))
print("In ten year you will be {} years old".format(int(age) + 10))




#Additional text formatting
print("1 2 3 4 5")
print("1\n2\n3\n4\n5") #\n to break line
print("My favorite book is \"Harry Potter\" J.K.Rowling") #Escape character
















