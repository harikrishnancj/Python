"""Exercise 3
Name your file: BodyMassIndex.py
Write a program to calculate your BMI and give weight status. Body Mass Index (BMI) is an internationally used measurement to check if you are a healthy weight for your height.The metric BMI formula accepts weight in kilograms and height in meters:
BMI= weight(kg)/height2(m2)
BMI Weight Status Categories table
BMI range - kg/m2   Category
Below 18.5                    Underweight
18.5 -24.9         Normal
25 - 29.9          Overweight
30 & Above     Obese
An example run of the program (numbers in bold are typed in by the user)
Enter your weight in (kg): 75
Enter your height in (m): 1.70
Your BMI is: 25.95
You are in the “overweight” range.
"""

w=float(input("Enter your weight in (kg):"))
h=float(input("Enter your height in (m):"))
BMI=w/h**2

if BMI<18.5:
    cat="Underweight"
elif BMI>=18.5 and BMI<=24.9 :
    cat="Normal"
elif BMI>=25 and BMI <=29.9:
    cat="Overweight"
else :
    cat="Obese"


print(f'You are in the “{cat}” range.')