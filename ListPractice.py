l=[20,0,15,10,3]
# l.remove(15)
# l.pop(2)
# print(l)
l.sort(reverse=True)
print(l)
# print(id(l))
x=l.copy()
# print(id(x))
print(x)
x=['dog','cat','rat']
y=['dog','cat','rat']
z=['DOG','CAT','RAT']
print(x==y)
print(x==z)
print(x!=z)
x=[50,20,30]
y=[50,10,100,120,170]
print(x>=y)
x=['dog','cat','rat']
y=['dat','cat','rat']
print(x>y)
x=[10,20,30]
print(10 in x)
print(100 in x)
print(100 not in x)
x.clear()
print(x)
# Nested Lists
l=[10, 20, [30,40]]
print(l)
print(l[0], "---", l[1],"------", l[2][0], "--------", l[2][1])
l=[[10,20,30],[40,50,60],[70,80,90]]
print(l)
for x in l:
    print("Print Row Wise")
    print(x)
print("print matrix Wise:")
for i in range(len(l)):
    for j in range(len(l[i])):
        print(l[i][j], end=" ")

    print()  





    # List comprehensions


# i want list of square of 10 numbers
l=[]
for x in range(1,11):
    l.append(x*x)

print(l)
# another way to print this
l1=[x*x for x in range(1,11)]
print(l1)
l2=[x for x in l1 if x%2==0]
print(l1)
print(l2)
l=['rachit','nikant','sumit','ankur','juhi']
# l=[w[0] for w in l]
l=[w for w in l if len(w)>4 ]
print(l)
n1=[10, 20, 30,40]
n2=[30,40,50,60]
n3=[x for x in n1 if x not in n2]
print(n3)
words="the quick brown jumps over the lazy dog".split()
print(words)
l=[[w.upper(), len(w)] for w in words ]
print(l)
