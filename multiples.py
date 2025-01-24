"""Exercise 7
Finding the multiples of a number using loop"""

a=int(input("Enter the number whose multiples needed to find :"))
b=int(input("Enter the number of multiples to found :"))

for i in range(1,b+1):
    print(f"{a}x{i}={a*i}")