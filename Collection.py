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