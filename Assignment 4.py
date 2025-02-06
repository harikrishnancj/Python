#What does the len() function do in Python? Write a code example using len() to find the length of a list.
# Ans
"""len() is used find length of string,length of list,set etc.... it's an in built function"""

a=input("Enter element with comma between them for finding list length:").split(",")
print("Length of list :",len(a))
print(a)
print("----------------------------------------------2-------------------------------------------------------------")
#Write a Python function greet(name) that takes a person's name as input and prints "Hello, [name]!".


def greet(name):
    print(f"Hello,{name}!")


b=input("Enter the name:").capitalize()
greet(b)
print("------------------------------------------------3-----------------------------------------------------------")
#Write a Python function find_maximum(numbers) that takes a list of integers and returns the maximum value 
# without using the built-in max() function. Use a loop to iterate through the list and compare values.

num= list(map(int, input("Enter numbers separated by comma for max finding: ").split(",")))
max=0
for i in num:
    if i>max:
        max=i
    
print("maximum value :",max)
print("-------------------------------------------------4----------------------------------------------------------")        
#Explain the difference between local and global variables in a Python function. 
# Write a program where a global variable and a local variable have the same name 
# and show how Python differentiates between them.
#Ans
"""Local variables are declared inside a function and can only be accessed within that function, whereas global variables are declared outside of functions and can be accessed by all functions in the program.
 If a local variable inside a function has the same name as a global variable, the function will prioritize the local variable by default.
 To modify a global variable inside a function, the global keyword must be used."""

x=20
def loc():
    x=10
    print("local value :",x)
def key():
    global x
    x=50
    print("Using Global keyword modifing :",x)
print("global :",x)
loc()
key()
print("after modification",x)
print("-------------------------------------------------5----------------------------------------------------------") 
"""Create a function calculate_area(length, width=5) that calculates the area of a rectangle.
 If only the length is provided, the function should assume the width is 5.
  Show how the function behaves when called with and without the width argument.
"""

def calculate_area(leng,width=5):
    return leng*width

l=float(input("Enter the length:"))

o=input("is there a width value (y/n):")
if o.lower()=='y':
    w=float(input("enter the width:"))
    area=calculate_area(l,w)
else:
    area=calculate_area(l)

print("Area :",area)