from sys import argv
# command line arguments::::::::::::::::::
print(argv)
print(argv[0])
print(argv[1:])
print(argv[:])
print(len(argv))
for x in argv:

    print(x)
print("slice operatoe results", argv[1:3])
# sum=0
# for p in argv:
    
#     sum) = sum + int(p)
#     print("sum is :::", sum)
print(argv[1])
print(argv[1]+argv[2])
print(int(argv[1])+int(argv[2]))
print(argv[7:1000])
# sep=',' attributes

a,b,c=10,20,30
print(a,b,c)
print(a,b,c, sep=',')

# End=',' attribute
print("hello", end=',')
print("student",end=',')
print("python",end=',')
print("Very Easy",end=',')

l=[10,20,30,40]
t=(10,20,30,40)
s={10,20,30,40}
print(l, end='')
print(t, end='')
print(s, end='')


name="Durga"
l=[10,20,30,40]
print("hello %s the list is: %s" %(name,l))

# Replacement Operatoe::::::::::::::::::



name="Durga"
salary=10000
gf="Sunny"
print("hello {0} your salary is {1} and your Girl Friend {2}".format(name,salary,gf))
print("hello {} your salary is {} and your Girl Friend {}".format(name,salary,gf)) # default 
print("hello {x} your salary is {y} and your Girl Friend {z}".format(x=name,y=salary,z=gf))

name=input("Enter Name:::::")
if name=="Durga":
  print("Hello %s Good Morning" %name)
else:
   print("Hello Guest GooD Morning")
print("How are You??")



# elif
name1=input("Enter the name::")
if name1=="Rc":
  print("Rc")
elif name1=="PC":
 print("PC")
else:
    print("nothing")  