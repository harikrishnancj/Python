"""Exercise 4
Write a Python program to receive 3 numbers from the user and print the greatest among them.
"""
a=list(map(int,input("enter the numbers separated by comma :").split(',')))
m=max(a)
print(f"greatest amoung them {m}")