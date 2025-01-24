"""Exercise 8
Write a program to print the inputted value as it is and break the loop if the value is 'done'.
Example run of the program
:hello there
hello there
:finished
finished
:done
Done
"""
i=1
while i>0:

    a=input(":")
    if a.lower()=='done':
        print('Done')
        break
    print(a)