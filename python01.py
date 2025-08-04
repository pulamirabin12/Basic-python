# list comprehension in python -> output is a list
# like ternary operator similar to one line code 
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in list1:
    print(i*2)  #   print each element in the list 

#expression -> [expression for item in iterable]
#expression -> [expression for item in iterable if condition]
output1 = [i*2 for i in list1 if i%2==0]
print(output1)  # [4, 8, 12]    

#wap to print the square of even numbers from 1 to 100
output2 = [i**2 for i in range(1,101) if i%2==0]
print(output2)  # [4, 8, 12, 16, 20
#wap to print the multiplication table of 7 using list comprehension
output7= [i*7 for i in list1]
print(output7)  # [7, 14, 21, 28, 35   

#global variable and local variable
abc = 10 # global variable
def cal():
    bcd= 20 # local variable
    print("This is a name function")
    return abc+bcd
    print(bcd)
print(cal())
print(abc)


# calculator app using fun -> add, sub, div, mul, **, exit and ask the 3 input for the user 
# 2 will be numbers and 1 will be option and use recursion to call the function again
#and again until the user wants to exit using recursion


def add(num1, num2):
    return num1+num2
def sub(num1, num2):
    return num1 - num2
def div(num1, num2):
    return num1 / num2
def mul(num1, num2):
    return num1 * num2
def expo(num1, num2):
    return num1 ** num2
def calculator():
    while(True):
            print("Welcome to our Calculator App")
            print("1. Add")
            print("2. Subtract")
            print("3. Divide")
            print("4. Multiplication")
            print("5. Exponentiation")
            print("6. Exit")
            options = int(input("select your option: "))
            list_of_options = [1,2,3,4,5]
            if options in list_of_options:
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))
                if options == 1:
                    print(f"Result: {add(num1, num2)}")
                    return calculator()
                elif options == 2:
                    print(f"Result: {sub(num1, num2)}")
                    return calculator()
                elif options == 3:
                    print(f"Result: {div(num1, num2)}")
                    return calculator()
                elif options == 4:
                    print(f"Result: {mul(num1, num2)}")
                    return calculator()
                elif options == 5:
                    print(f"Result: {expo(num1, num2)}")
                    return calculator()
            else:
                print("Exiting the calculator app")
                return calculator()
            
calculator()


