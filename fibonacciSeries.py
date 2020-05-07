import random
n = random.randint(50, 150)
print(n)
fib1 = 0
fib2 = 1 
fib3 = 0
sum = 0 

while(fib3<n):
    print(fib3)
    if (fib3%2==0):
        sum = sum + fib3
    fib1 = fib2
    fib2 = fib3
    fib3 = fib1 + fib2

print("Sum of even numbers in series is", sum)