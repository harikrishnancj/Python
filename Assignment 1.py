#Exercise 1
 
print('Bob')
print('ST1001 ')
print('bob@gmail.com ')

#Exercise 2 

print("--------------------------------------------------------------------")
print('Bob \nST1001 \nbob@gmail.com ')

#Exercise 3

print("--------------------------------------------------------------------")
n1=14
n2=7
print(f'{n1}+{n2}={n1+n2}')
print(f'{n1}-{n2}={n1-n2}')
print(f'{n1}*{n2}={n1*n2}')
print(f'{n1}/{n2}={n1/n2}')

#Exercise 4

print("--------------------------------------------------------------------")

for i in range(1,6):
    print(i)

#Exercise 5

print("--------------------------------------------------------------------")
print('"SDK" stands for "Software Development Kit", whereas ')
print('"IDE" stands for "Integrated Development Environment". ')

#Exercise 6

print("--------------------------------------------------------------------")
print("python is an \"awesome\" language.")
print("python\n\t2023")
print('I\'m from Entri.\b')
print("\65")
print("\x65")
print("Entri", "2023", sep="\n")
print("Entri", "2023", sep="\b")
print("Entri", "2023", sep="*", end="\b\b\b\b") 

#Exercise 7

print("--------------------------------------------------------------------")

num=23
txtnum="57"
dec=98.3
print(type(num))
print(type(txtnum))
print(type(dec))
sum=num+int(txtnum)+dec
print(type(sum))
print(sum)

#Exercise 8

print("--------------------------------------------------------------------")

total_day=365
total_hours_inday=24
minute=60

t=total_day*total_hours_inday*minute
print(t,"total minute in a year")

#Exercise 9

print("--------------------------------------------------------------------")

a=input("Enter your name :")
print(f'Hi {a}, welcome to Python programming :)')

#Exercise 10

print("--------------------------------------------------------------------")
a=int(input("enter the pounds to be covereted :"))
dollar=a*1.23
print(f"IN dollars :{dollar}")