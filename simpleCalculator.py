import sys
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

#This function add two numbers 
def add(x, y):
    return x+y 

#This function subtracts two numbers 
def subtract(x, y):
    return x-y 

# This function multiplies two numbers 
def multiply(x, y):
    return x*y

#This function divides two numbers 
def divide(x, y):
    return x/y 

print("Select operation:")
print("1: Add")
print("2: Subtract")
print("3: Multiply")
print("4: Divide")

choice = int(input("Enter your choice(1/2/3/4)"))
if choice == 1:
    print("sum=", add(num1, num2))
elif choice ==2:
    print("difference=", subtract(num1, num2))
elif choice ==3:
    print("product=", multiply(num1, num2))
elif choice == 4:
    print("Quotient=", divide(num1, num2))
else:
    print("Invalid input")