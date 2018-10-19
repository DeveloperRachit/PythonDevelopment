# import math as m will get error
# import math
# from math import sqrt,pi
from math import * # all classes imported 
# print (math.sqrt(16))
# print(math.pi)
print (sqrt(16)) # directly we can use it like sqrt and pi 
print(pi)

# sqrt()
# ceil()
# floor()
# pow(x,y)
# factorial()
# gcd()
# sin()
# cos()

r=int(input("Enter the Radius::::"))
Area=pi*r*r
print(Area)

# Input Output statement
# x=input("Enter the no")
x=int (input("Enter the no"))
print(type(x))
# y=input("Enter the 2nd no.")
y=int(input("Enter the 2nd no."))
print(type(y))
# i=int(x)
# j=int(y)
print("The Sum :::", x+y)


print("the sun is::", int (input("Enter the no"))+int (input("Enter the 2nd no")))
# how to read multiples values from keyboards 


# a, b=[int(x) for x in input ("Enter 2 numbers::").split()]
# print("The Product", a * b)
# a, b=[float (x) for x in input ("Enter 2 numbers::").split(',')]




# eval() method also we have 
x=eval("10+20+30+40")
print(x)

# command line arguments
