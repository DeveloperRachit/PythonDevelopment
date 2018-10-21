for i in range (6):
    for j in range(6):
        print("*",end="")

    print()        

num=int(input("Enter a Number"))
 
for i in range(1,num+1):
     print(" "*(num-i),end="")   
     for j in range(1,i+1):
        print(num+1-j,end="")
     for k in range(2,i+1):
        print(num-i+k, end="")    
     print()
for i in range(1,num+1):
     print(" "*i,end="")
     for j in range(1,num+1-i):
         print(num+1-j,end="")
     for k in range(2,num+1-i):
         print(i+k,end="")
     print()

for i in range(1, num+1):
    print(" "*(num-i),end="")
    for j in range(i,i+1):
        print(chr(64+i),end="")                
        if i>=2:
            print(" "*(2*i-3), end="")   
            for k in range(i,i+1): 
                print(chr(64+i),end="")  
    
    print()     


    # Tree printing
    
for i in range(1, num+1):
    print(" "*(num-i),end="")
    for j in range(i,i+1):
        print("* ",end="")                
        if i>=2:
            # print(" "*(2*i), end="")   
            for k in range(i,2*i-1): 
                print("* ",end="")
    print() 
    for a in range(1,num+1):
        print(" "*(num-i),end="")    
        for b in range(a,a+1):
          print("* ",end="")                
          if i>=2:
            # print(" "*(2*i), end="")   
            for k in range(i,2*i-1): 
                print("* ",end="")

     
        print()            





#TRAJJJJJJJJJJJJJJJJJ


for i in range(1, num+1):
    print(" "*(num-i),end="")
    for j in range(i,i+1):
        print("* ",end="")                
        if i>=2:
            # print(" "*(2*i), end="")   
            for k in range(i,2*i-1): 
                print("* ",end="")
    print() 
for i in range(1, num+1):
    print(" "*(num-i),end="")
    for j in range(i,i+1):
        print("* ",end="")                
        if i>=2:
            # print(" "*(2*i), end="")   
            for k in range(i,2*i-1): 
                print("* ",end="")
    print()
for i in range(1, num+1):
    print(" "*(num-i),end="")
    for j in range(i,i+1):
        print("* ",end="")                
        if i>=2:
            # print(" "*(2*i), end="")   
            for k in range(i,2*i-1): 
                print("* ",end="")
    print()    


for i in range(1, num+1):
     print(" "*(num-1),end="")
     for j in range(i,i+1):
        print("* ",end="")

     print()     