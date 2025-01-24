
"""Exercise 5
Find the factorial of a given number using loops(note the number is received from the user)
"""

a=int(input("Enter the number: "))
b=a+1
n=1
for i in range(1,b):
    n*=i
print(f"factorial of {a} = {n}")