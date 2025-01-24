"""Exercise 1
Name your file: MonthNames.py
Write a program that reads an integer value between 1 and 12 from the user and prints output the corresponding month of the year.
An example run of the program (numbers in bold are typed in by the user)
Enter the month: 3
Month 3 is March"""

a=input("Enter the month: ")

dic={
    "1":"January",
    "2":"February",
    "3":"March",
    "4":"April",
    "5":"May",
    "6":"June",
    "7":"July",
    "8":"August",
    "9":"September",
    "10":"October",
    "11":"November",
    "12":"December",
}
b=dic.get(a,"not a valid number")
print(f'Month {a} is {b}')