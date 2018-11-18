def f1():
    print("f1 function")
class one:
    def info(self):
        print("info function")
f1()
s=one()
s.info()        

l=[10,20,30,40,10,50,10]
print(len(l))
print(l.count(10))
print(l.index(10))
target=int(input("Enter the value to Search:::"))
if target in l:
    print(target,"available and it's First occurence is at:", l.index(target))
else:
    print(target,"not available")    

l=[]
l.append(10)    
l.append(20)
l.append(30)
l.append(40)
l.append(50)
print(l)
# l.insert(1,50)# if we want to added 50 at a specified location
l.insert(50,777)
print(l)
l.insert(-10,999)
print(l.index(777))
print(l.index(999))

# TO add all elements to list upto 100 which are visible by 10
l=[]
for x in range(101):
    if x%10==0:
        l.append(x)
    else:
        continue

print(l)        
             
l1=['chicken', 'Fish', 'mutton']
l2=['kfc','RC','FO']
print(id(l1))
l1.extend(l2)
print(l1)
print(l2)
print(id(l1))


# sorted 

t=[10, 30, 40, 20, 5, 11]
t.sorted()
print(t) 