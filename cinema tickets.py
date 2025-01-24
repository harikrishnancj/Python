"""
Exercise 2
A certain cinema currently sells tickets for a full price of 6 pounds, but always sells tickets for half price to people who are less than 16 years old, and for a third of the price for people who are 60 years old or more.
An example run of the program (numbers in bold are typed in by the user)
Enter your age: 63
Your ticket costs £2.00
"""

age=int(input("Enter your age: "))
price=6.00
if age <16:
    Tprice=price/2
elif age>=60:
    Tprice=price/3
else:
    Tprice=price

print(f"Your ticket costs £{Tprice}")