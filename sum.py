def sum(a,b):  
            
 print ("Printing within Function")  
 #print(a+b)  
 return a+b  
			
			
print(sum(5,10))			


square=lambda x1: x1*x1 #anonymous Function that is used by lambda keyword  
  
#Calling square as a function  
print("Square of number is",square(10))  
'''
def msg():  
           a=10  
           print ("Value of a is",a)  
           return  
  
msg()  
print (a)#it will show error since variable is local 
'''


b=20  
def msg1():  
  a1=10  
  print ("Value of a is",a1)  
  print ("Value of b is",b)  
  return  
  
msg1()  
print (b)  




n=input("Enter your expression");  
print ("The evaluated expression is ", n) 


p =input("Enter your name ");  
print ("Welcome ", p)  



prn=int(input("Enter Principal"))  
r=int(input("Enter Rate"))  
t=int(input("Enter Time"))  
si=(prn*r*t)/100  
print ("Simple Interest is ",si)     
