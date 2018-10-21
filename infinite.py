for i in range(5):
    for j in range(i):
        print("* "*i)
print()        


for i in range(4):
    for j in range(4):
      print("i={} and j={}".format(i,j))
a=0
# while True:
# while 1234:
while -1: 
    print("Hello")
    a+=1
    if a==5:
        break 
# Transfer Statements
# break--------=> based on some condition if u want to break loop execution

# continue
# pass
for i in range(10):
        if i==7:
          print("Processing is enough ----plz break it")
          break
        print(i)

cart=[10, 20, 30,40,600,500,400]
for item in cart:
        if item>500:
                print("Sorry we can't process this order")
                break

        print("Processing Item",  item)

for i in range(10):
        if i%2==0:
           continue
        print(i)
numbers=[10,20,0,5,0,30]
for n in numbers:
        if n==0:
          print("Hey how we can dvide it by Zero")
          continue
        print("100/{}={}".format(n,100/n))
cart=[10, 20, 30,40,600,50,60,70]
for item in cart:
        if item>500:
                print("Sorry we can't process this order")
                break

        print("Processing Item",  item)

else:
        print("Congrates all item processed successfully") # if break stat. is execute then else part will not get execute


        # Pass is an empty statement 

#  it is null statement 
#  it won't do anything
# # print("pass look ")
def f1(): # function methods in py
        print("f1")
def f2():
   pass #empty block

f1()
f2()             

for i in range(100):
        if i%10==0:
                print(i)
        else:
                pass



x=10
print("variable value is::::::",x)
del x
print("after deleting",x)
