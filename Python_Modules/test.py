from sys import argv
print(len(argv))
print(argv)

for x in argv:
    print(x)
a,b,c=10, 20,30
print(a,b,c)
print(a,b,c,sep=',')
print("hello",end='')
print("student",end='')
print("python" ,end='')

print(10,20,30,40, sep=':',end='...')
print(10,20,30,40, sep='-')
print("the value is %a" %a)
print("a value is %i and b value is %i" %(a,b))


l =[10,20,30,40]
name="durga"
print("hello %s the list is : %s" %(name,l))


name="Durga"
salary=10000
gf="sunny"
print("hello {0} your salary {1} gf {2}is waiting".format(name, salary, gf))
n=int(input("Enter the rows:"))
for i in range(1,n+1)
  for j in range(1, i+1)
     print("*", end='')
print()     