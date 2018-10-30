s1="Rachit"
s2='durga'
print(s1)
# print(type(s1))
print(s2)
a="this is ' single quotes"
print(a)
b='this is \' single quotes symbols'
print(b)
a='this is " double quotes'
print(a)
a='this is \" double quotes'
print(a)

# a='these are ' and " symbols'  will get error by using that
a='these are \' and \" symbols '
print(a)
a='''these are ' and " symbols'''
print(a)
a="durga"
print(a[0])
s=input("Enter Any String:::::")
i=0
for x in s:
    print("the character present at positive index:{} and at negative index:{} is :{}".format(i,i-len(s),x))
    i+=1

    # multilines String::::::;;

s='''Durga
       software
        Solutions'''

print(s)

A = "spam" 

B = A# references is same as A 
del A
print(id(B))
B = "shrubbery"

# print(id(A))
print(id(B))


A = ["spam"]
B = A
print(B)
print(len(B))
B[0] = "shrubbery"
# for i in B:
#         print(i)
print(len(B))


A = ["spam"]
B = A[:]
B[0] = "shrubbery"
print(A)


'''

1. No: A still prints as "spam". When B is assigned to the string "shrubbery", all that
happens is that the variable B is reset to point to the new string object. A and B
initially share (i.e., reference/point to) the same single string object "spam", but two
names are never linked together in Python. Thus, setting B to a different object has
no effect on A. The same would be true if the last statement here were B = B +
'shrubbery', by the way—the concatenation would make a new object for its result,
which would then be assigned to B only. We can never overwrite a string (or number,
or tuple) in place, because strings are immutable.

2. Yes: A now prints as ["shrubbery"]. Technically, we haven’t really changed either
A or B; instead, we’ve changed part of the object they both reference (point to) by
overwriting that object in place through the variable B. Because A references the
same object as B, the update is reflected in A as well.

3. No: A still prints as ["spam"]. The in-place assignment through B has no effect this
time because the slice expression made a copy of the list object before it was assigned
to B. After the second assignment statement, there are two different list
objects that have the same value (in Python, we say they are ==, but not is). The
third statement changes the value of the list object pointed to by B, but not that
pointed to by A.
'''


# Empty String
s=''
print(s)
# Double quotes, same as single
S = "spam's"
print(S)
# Escape sequences
S = 's\np\ta\x00m'
print(S)

# Triple-quoted block strings
S = """...multiline..."""
print(S)
# Raw strings (no escapes)
S = r'\temp\spam'
print(S)
# Byte strings in 2.6, 2.7, and 3.X (Chapter 4, Chapter 37)
B = b'sp\xc4m'
print(B)
# Unicode strings in 2.X and 3.3+ (Chapter 4, Chapter 37)
U = u'sp\u00c4m'
print(U)
# Concatenate, repeat
s='01234567890'
print(s[0:7:1])
print(s[0:7:2])
print(s[0:7])
print(s[0:])
print(s[::])
print(s[::-1])
# string matematical operators like::::: +,*

s='durga'+'soft'
print(s)
# s='durga'+10=====> error

s='durga'+'10'
print(s)
# python Strings Functions and methods:::;;


s1='durh'.capitalize()
print(s1)
s2="Java T point";

print(s2.count("a",0,8))

# WAP to access each character of string in forward direction and backward Direction
# -------------------------------------------------------------------------------------------

# s[:]==========>Forward Direction
# s[::-1]=======>Reverse Direction
# while Loop
s=input("Enter the String")
n=len(s)
i=0
print("Data in Forward Direction")
while i<n:
        print(s[i], end="")
        i=i+1

print("Data In Backward Option")
i=n-1
while i>=0:
        print(s[i])
        i=i-1
print()

print("Data In Backward Option")
i=-1
while i>=-n:
        print(s[i])
        i=i-1






# Remove Duplicate Characters From the Strings


# str1="missippi"
# n=len(str1)
# index=0
# i,j=0,0
# for i in range(i,n):
#      for j in range(0,i):
#         if str1[i]==str1[j]:
#                 break
#         index=index+1
#         if j==i:
#            str1=str1[i]

           
# print(str1)


# Membership operators::::::::;





