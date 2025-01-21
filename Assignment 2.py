"""Topic :List
Exercise"""


l=[8,9,10,11,12]
print("list =",l)
b=[1,3,4]
l.extend(b)
l.append(5)
for i in l:
    print(i)

print("-------------------------------------------------------------------------------------")
"""
Topic: Dictionary
Exercise
"""

d={'name':'jhon','age':18,'address':'New york'}
print(d)
d['phone']=1234567890
print("dictionary",d)


"""Topic: Set
Exercise 
"""
print("-------------------------------------------------------------------------------------")
s={1,2,3,4,5}
print("sets",s)
s.add(6)
print(s)
s.discard(3)#s.remove(3)
print(s)

"""Topic:Tuple
Exercise """
print("-------------------------------------------------------------------------------------")
t=(1,2,3,4)
a=len(t)
print(a,"is the lenth of tuple")