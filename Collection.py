empty=()
print(type(empty))
one=("carry",)
print(type(one)) # tuple need to use ,comma after  
# print(one)
# print(one[0:])
# print(one[:1])
Names="Albert","Brenda", "cecil", "Donna" 
'''
# it's also possibe to drop the parentheses for tuple that have 
at least two  items where the meaning is ambiguous
'''
print(Names[:3])
print(type(Names))
'''
We create a tuple of names, then take a slice of the first three items, and then
look at the item at index position 1. Like all Python sequences, the first item is
at position 0:
'''
names =Names[0], Names[1], "Bernadette", Names[2], Names[3]
print(names)
print(type(names))
names=Names[:2],"Bernadette",Names[2:]
print(names)
print(names[2])#tuple of tuples
print(len(names))
# convert any sequence in the tuple
check=tuple("some text")
print(check)
'''
List Examples Below kindly check that 
'''
print("===================================================\nList")
'''
The list type is an ordered sequence type similar to the tuple type. All the
sequence functions and the slicing that we have seen working with strings and
tuples work in exactly the same way for lists. What distinguishes tuples from
lists is that lists are mutable and have methods that we can use to modify them.

And whereas tuples are created using parentheses, lists are created using
square brackets (or by using the list() constructor).
'''


Fruit=["Apple", "Banana", "guava"]
print(Fruit)
print(type(Fruit))
print(Fruit[:2])
print(Fruit[:-2])
Fruit.insert(3, "Graphes")#insertion of a elements
print(Fruit)
del Fruit[3]
print(Fruit)
#  Now we will do the same thing using slicing:
Fruit[3:3]=["Graphes"]
print(Fruit)
Fruit[2:3]=[]
print(Fruit)
print("Apple" not in Fruit)
Frui=["Gua", "Ginger"]
print(Fruit+Frui)
# print(Fruit.extend(Frui))
print(len(Fruit))
print(Fruit.count("Apple"))
print(Fruit.index("Banana"))
Fruit.append("switch")
print(Fruit)
Fruit.insert(5,"Banana1")
print(Fruit)
Fruit.remove("Banana1")
print(Fruit)
Fruit.pop()
print(Fruit)
Fruit.reverse()
print(Fruit)
Fruit.sort()
print(Fruit)



L=(10, 20, [2, 6])
print(L)
print(len(L))
print(type(L))
print(type(L[2]))# particular elemnt Type

r=range(10)
print(type(r))
print(r)
for i in r: #just like a each loop in java
    print(i)

print("++++++++++++++++++++++++++")
print(r[5])
print("========================================================\n @@@@@@@@@@\t %%%%%%%%%%%%%%%%%%%%%")
# r[0]=777# this is invaliid
for i in range(10, 50, 5):# 5 is diffrences between 10  to 50 printing element will print in that sequence
    print(i)
'''
it is applicable for interger value only Range()


y=range(10.5, 50.66)
for i in y:
    print(i)
'''
print("==========Set===========")

s={10, 20, 30}# duplicate are not allowed in case of Set
print(s)
# print(s[0])
'''
Traceback (most recent call last):
  File "Collection.py", line 111, in <module>
    print(s[0])
TypeError: 'set' object does not support indexing
insertion Order n
indexing n
duplicate n
hetrogeneous y
slicing 


'''
s.add("Rachit")
print(s)
s.remove(20)
print(s)
s1=set()
for i in range(10):
    s1.add(i)

print(s1)

s2={'a','b','c','d','ce'}
print(s2)#order ia not preserved 
s={10, 20, 30}
fs=frozenset(s)
print(type(fs))
print(fs)
# frozenset is immutable we can't cahnge and can't use any method like add remove Bytes in Immutable and Byte array is immutable

# [] list 
# ()--tuple 
# {} Set 
# {} Dict ----having Key and value pair represented by {} curly braces given below also.
print("#####################################################{}DICT::::::#############################")
d={100:'Rachit', 200: 'Mohit', 300:'rajan'}
print(type(d))
print(d) 
d1={}
d2=set()# empty set declaring way
print(type(d1))
print(type(d2))
print(d[100])
d1[100]='sumit'
d1[200]='soman'
print(d1)
d1[100]='sumit1' # when it will get duplicacy in Key then it will interchange the old value by the new value but not allowed duplicate key
print(d1)


l=[10, 20 ,30 ,40]
b= bytes(l)
print(type(b))
# b[0]=100 error just because of immutable
# should be range 0 to 256
print(b[0])

l=[10, 20 ,30 ,40]
b= bytearray(l)
print(type(b))
b[0]=100 # in the case of Bytearray this is not error just because of mutablility
print(b[0])
# range to represent a range of values 
# range(10) ---->  0 to 9
# range(10, 30)---->  10 to 29


# fuctions in Python:



def f1():
  print("hello don't be like")

f1()




def f2():
 a=10

print(f2()) # None will return becoz there no value and not returning 
# Using Pass Keyword 

def f3():
#  if we will not write any thing inside Function then it will throw error like
# this is the error  SyntaxError: unexpected EOF while parsing
# if this function is not doing anything just Pass the keyword using Pass like below 
  pass #better way to keep[none]

# Escape Character :
# ---------------------
# \n, \t, \r, \b , \', \", \\, \v
print("hello \n World")
print("hello \t World")
# print("hello \r World")
# print("hello \b World")
print("hello \"Durga sir \" World")
print('hello "Durga sir" World')
print('''hello 'Durga sir' and "great" World''')
print("""hello 'Durga sir' and "great" World""")
print("hello \'Durga sir\' and \"great\" World")
#=---------- Constants--------- constant method is not applicable in python

'''
Operators:::::::::::::
Arithmetic
relational or comparison 
logical
bitwise
Assignment
Special
----------------
// floor division Operator
** Exponent Operator or power Operator










'''


# if both values are INT then result will get INT
# if one is Float then will get Answer Float
a=10.5
b=2
print("a+b",a+b )
print("a-b",a-b )
print("a*b",a*b )
print("a/b",a/b )
print("a%b",a%b )
print("a//b",a//b )
print("a**b",a**b )
print("a/b",10/3 )
print("a//b",10//3 )# it will have INT value only  
# Opreators for String(str)

print("print"+'3')# if you are trying to use like this 'print'+ 3 u will get error because python treated 3 as a int 
print('print'+ str(3) )
# String Manilpulation Operator

print('print' * 3)# Exponential Operator 
# print('print' * '3') go to get error one arg should be int and 2nd must be Str
# print('print' * 3.0)# this is also not applicable because of Floating no.
print(2 * 'print' )
print(10** -2)
print((10+2j)** (10+3j))
# print(10/0)   error
# print(10%0)  erroe
print(10** 0)# 1


# ===============Relational Operators==============
print("a<b", a<b)
print("a<=b", a<=b)
print("a>b",a>b)
print("a>=b",a>=b)


a=True
b=False


print("a<b", a<b)
print("a<=b", a<=b)
print("a>b",a>b)
print("a>=b",a>=b)


a=10
b=20

if(a>b):
  print("A is greater than B")
else:
  print("A is not greater than B")
# no zero value is true and zero is false
  print('a'==97)# ascii value also by default it take as like JAva
  print(10==3+7==2*5==5+5)
  print((10+2j)==(10+2j))
  print((10+2j)=='durga')
  print(10==10.0)
  print(10 and 20)# X and Y if x evaluate to false then return x otherwisw return y
  print(0 and 20)
  print(1 and 'durga')
  print(0 and 'durga')
  # X or y if x evaluate to True then Returns x otherwise return y
  print(10 or 20)
  print(0 or 20)
  print(0 or 0)

  # Not X:: this operator always return boolean value
print(not 10)
# empty string is treated as False
print(not '')
print(0 or True)
print(10 or 10/0)
# print(0 or 10/0) error

# and===> if both arg  are true then only true
# or===> if atleast one arg is true then true
# not ===> 
# BitWise Operator
# ---------------------------------
# & | ^ ~ << >>
# applicable for int and  boolean
# & if both bits are 1 then only 1 otherwiswe 0
# | if atleast bits are 1 then only 1 otherwiswe 0
# ^ x-or ==> if both arguments are differ then 1 otherwise 0
# ~  bit wise complement operator 1====>0 and 0======>1
# << bit wise left shift
# >> bitwise right shift
# 4 & 5===> 100  or 101==> 100===>4 ans
# 4 | 5===> 100  and 101==> 101===>5 ans
#  4 ^ 5===> 100  x-or 101==> 001===>1 ans
# ~4==>===> 100====>>>011===>>>>3 ans      ~ means -4
print(4 & 5)
print(4 | 5)
print(4 ^ 5)
print(~ 4)

# 1's complements ans 2 's complements will get applying 
print(~ True)# same as ~1 

# << left shift
# >> right Shift

print(10<<2)
print(-10>>2)
# assignment op/
x=10
x+=10
# print(x)
# print(++x)
# ternary operator
# p=(10>5)?'hello': "wrong"
# print(p)
# a=int(input("Enter the First Number:::"))
# b=int(input("Enter the second Number:::"))
# c=int(input("Enter the Third Number:::"))
# max=a if a>b and a>c else b if b>c else c
# print("Max Value::", max)
'''
a=int(input("Enter the Number:::"))
b=int(input("Enter the Second Numbers:::"))
print("Both are equals" if a==b else "First number is greater than second" if a>b else "First Number is smaller than Second Number")
'''

# ::::::::::::::Special Operators :::::::::::::::::|
# --------------------------------------------------

# 1. Identity  Operator=====> Address comparison purpose (Refernces Variable)
# 2. Membership Operator====>

a=10
b=10
print(a is b)# 1.
print(a is not b) 
a="durga"
b="durga"
print(id(a))
print(id(b))
print(a is b)
a=[10,20,30]
b=[10,20,30]
print(id(a))
print(id(b))
print(a is b)# address Comparison Identity  Operator
print(a==b)# content comparison  Identity  Operator

# +++++++++++Membership operator++++++++++++++++++
# in , not in
list1=[10,20,30,40]
print(10 in list1)
print(60 not in list1)

S="hello this is rachit !!!!!!!"
print("hello" in S)
print("is" in S)
print(" " in S)
print("he" not  in S)
print("R" in S)

# ++++++++Operator precedences++++++++++++++
print(10+3*2+(10+80))

# () parentheses
# ** Exponential
# ~ - unary 
# * / %  // 







