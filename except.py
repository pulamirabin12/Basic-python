# error handling and exception
# try, except, else, finally
'''
print("Hi")
try:
    a = int(input("number : "))
    print(a)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
print("Hello World")

except Exception as e:
    print(e)
else:
    print("Hello code works successfully")
finally:
print("Finally block")

print("hello world")
'''
# wap using try, except, else, finally print the number is odd or not by using input from the user

try:
    def printOdd():
        b = int(input("Enter a number: "))
        if b % 2 != 0:
            print("Number is odd")
        else:
            print("Number is not odd")
    printOdd()
except Exception as e:
    print(e)
else:
    print("Hello code works successfully")
finally:
    print("Finally block")