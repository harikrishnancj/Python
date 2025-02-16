"""5 File and Exception Handling
Exercise 1: (score : 1) 
Write a Python program to read a file and display its contents Exercise 2: (score : 1)
Write a Python program to copy the contents of one file to another file Exercise 3: (score : 2)
Write a Python program to read the content of a file and count the total number of words in that file. Exercise 4:(score : 1)
Write a Python program that prompts the user to input a string and converts it to an integer. Use try-except blocks to handle any exceptions that might occur Exercise 5: (score : 1) 
Write a Python program that prompts the user to input a list of integers and raises an exception if any of the integers in the list are negative. Exercise 6: (score : 2) 
Write a Python program that prompts the user to input a list of integers and computes the average of those integers. Use try-except blocks to handle any exceptions that might occur.use the finally clause to print a message indicating that the program has finished running. Exercise 7 : (score : 2)
Write a Python program that prompts the user to input a filename and writes a string to that file. Use try-except blocks to handle any exceptions that might occur and print a welcome message if there is no exception occurred."""

with open("file.txt","r") as f:
    c=f.read()
    print(c)

print("------------------------------------------------------------2-------------------------------------------------------------")

with open("file.txt","r") as f:
    c=f.read()
with open("wrt.txt","w") as w:
    w.write(c)
print("------------------------------------------------------------3---------------------------------------------------------------")

with open("file.txt","r") as f:
    c=f.read()
    j=c.split()
    print("total umber of word",len(j))
print("------------------------------------------------------------4---------------------------------------------------------------")

try:

    a=input("enter the number:")
    print("Before conversion",type(a))
    b=int(a)
    print(b,"After conversion",type(b))
except ValueError :
    print("enter a numeric string!!!!!!!!")

print("--------------------------------------------------------------5-------------------------------------------------------------")

try:
    numbers = list(map(int, input("Enter a list of integers with space: ").split()))
    
    for num in numbers:
        if num < 0:
            raise ValueError("Negative numbers are not allowed!")

    print("List is valid:", numbers)

except ValueError as e:
    print(f"Error: {e}")

print("--------------------------------------------------------------6-------------------------------------------------------------")

try:
    d=list(map(int,input("Enter the list of integers with space :").split()))
    n=len(d)
    sum=0
    if(n==0):
        raise ZeroDivisionError
    for i in d:
        sum+=i
    average=sum/n
    print(f"Average :{average}")
except ZeroDivisionError:
    print("list is empty")
except ValueError:
    print("enter integers")
    
finally :
    print("Code executed")

print("--------------------------------------------------------------7-------------------------------------------------------------")

try:
    file_name =input("enter the file name :")
    z=input("enter the content to write in file :")
    with open(file_name,"w") as file:
        file.write(z)
    print("File writted")
except Exception as e:
    print(F"Error{e}")
finally:
    print("Thats done")