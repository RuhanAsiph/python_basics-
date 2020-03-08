'''Swap two numbers without using temporary variable. Prompt the user for input'''
num1 = int(input("Enter Number 1:"))
num2 = int(input("Enter Number 2:"))
print("Before swapping: \n num1={} \n num2={}".format(num1,num2))
num1,num2=num2,num1
print("After Swappin: \n num1={} \n num2={}".format(num1,num2))
