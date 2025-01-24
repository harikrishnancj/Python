"""Exercise 6
Reverse a number using while loop
"""

n=input("Enter the number :")

rev=""
while len(n)>0:
    rev+=n[-1]
    n=n[:-1]
print(f"reversed number :{rev}")