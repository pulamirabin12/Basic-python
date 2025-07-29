# operation and operands
#python 7->
#arithmetic operators
print("add",5+5)
print("sub",5-5)
print("mul",5*5)
print("div",5/5)
print("rem",5&5) # & ->remainder
print("power",5**2) #power
print("//",5//5)
#wap to print the sum of two number by asking input from the user
#f -> string {}
print(f"the sum of two number is {5+5}")
# assignment operators =-> numbers
# += -> numbers
a = 10
print(a)
a+=10
print(a)
a*=19
print(a)
a//=5
print(a)
a**=2
print(a)
a/=2
print(a)
a%=2
print(a)
# comparison operators
# == -> equal to    
# != -> not equal to
# > -> greater than
# < -> less than
# >= -> greater than or equal to
# <= -> less than or equal to
print(5==5) #True
print(5!=5) #False
print(5>5) #False
print(5<5) #False
print(5>=5) #True
print(5<=5) #True
# logical operators
# and -> both condition are true
# or -> one condition is true
# not -> opposite of the condition
print(5>5 and 5<5) #False
print(5>5 or 5<5) #True
#and 
print(True and True) #True
print(True and False) #False
print(False and True) #False
print(False and False) #False
#or
print(True or True) #True
print(True or False) #True
print(False or True) #True
print(False or False) #False
#not
print(not True) #False
print(not False) #True
# Identify operators -> is , is not , in , not in , issubclass , isinstance
a = 20
b = "20"
print(a is b) #False
print(a is not b) #True
# membership Operators -> in and not in -> bool
list1 = [1,2,3,4,5]
print(4 in list1)
print(6 not in list1)

# bitwise Operators -> |, &, ^, ~, <<, >>, ~
print(5&5)
print(5|5)
print(5^6)
# ternary operator -> condition ? value if true : value if false
age = 2
print("above 18" if (age>18) else "below 18")
#wap to print the number is odd or not by asking input from the user
num = int(input("Enter the number: "))
print("odd " if num%2 !=0 else "even")
#wap to print if the user can drive or not 
print("drive" if age > 21 else "below age")
# condition als -> if, elif, else, match
# if -> if condition is true then execute the block of code
# elif -> if condition is true then execute the block of code
value= int(input("enter the number: "))
if (value%2 !=0):
    print("the given number is Odd")
elif (value ==0):
    print("the given number is zero")
elif (value >90):
    print("the given number is above 90")
else:
    print("the given number is even")
# wap to print if the given value is fizz, buzz,fizzbuzz conditions are
# fizz -> number divide by 3
# buzz -> number divide by 5
# fizzbuzz -> number divide by both 3 and 5
num1= int(input("enter the number: "))
if (num1%3 == 0):
    print("Fizz")
elif (num1%5 == 0):
    print("Buzz")
elif (num1%3==0 and num1%5==0):
    print("FizzBuzz")
#match statement
    day = "sunday"
    match(day):
        case "monday":
            print("today is monday")
        case "tuesday":
            print("today is tuesday")
        case "wednesday":
            print("today is wednesday")
        case _:
            print("none of the above")
# wap to check if a number is positive , negative, or zero using if-elif-else.
num3 = int(input("Enter the number: "))
if (num3 > 0):
        print("The number is positive")
elif(num3 < 0):
        print("The number is negative")
else:
        print("The number is zero")
    
# Ask the user for number and print "High" if it is above 90, "Zero" if it is 0, or "other" otherwise
num4 = int(input("Enter the number: "))
if (num4 > 90):
    print("High")
elif (num == 0):
    print("Zero")
else:
    print("Others")
# Demonstrate the use of arithmetic operators by calculating the sum, difference, product, and a quotient of two numbers.
b = 10
c = 10
print(b+c)
print(b-c)
print(b*c)
print(b/c)
# Show how to use assignment operators (+=, -=, *=, etc.) with an example
d = 10
print(d)
d+=19
print(d)
d-=2
print(d)
d*=3
print(d)
# Wap to demonstrate the use of logical operators (and ,or, not) with boolean values
print(True and True) #True
print(True or False) #True
print(not True) #False