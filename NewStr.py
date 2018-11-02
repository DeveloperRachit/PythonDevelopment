# city=input("Enter Your City Name:::::::::::")
# list=["Hyd", "Delhi","Mumbai", "Banglore"]
# if city.strip() in list:
#     print("your City {} is available in your List".format(city))
# else:
#     print("Plz Enter Valid city")   
# No of occurence in string
'''
s=input("Enter main String")
subs=input("Enter substring")
flag=False
pos=-1
n=len(s)
count=0
while True:
    pos=s.find(subs,pos+1,n)
    if pos==-1:
        break
    print("Found at index:", pos) 
    flag=True
    count=count+1
if flag==False:
    print("Not Found")   
print("The number of occurence ::", count)    

# inbuild method we also having 
# count(subs) count(subs, begininndex, end index)
# print(s.count(subs))
# print(s.count(subs,1,8))
s=s.replace("difficult","easy")
# print(s.replace("difficult","easy"))
print(s)
'''


s='abababab'
# s1=s.replace('a','b')
print(s,"Address is before replcement:", id(s))
# print(s1,"Address is:", id(s1))

print("Adress is after Replacement:::",s.replace('a','b'),id(s))
# Spiliting of strings:::::::;;

s="30-10-2018"#"Durga software Solutions"
# l=s.split('-',1)
l=s.rsplit('-',1)# Reverese
print(l)
for x in l:
    print(x)

l=['durga', 'soft', 'solution']
s=' '.join(l)
print(s)    

s1="Python Classes by Durga Sir"
print(s1.upper())
print(s1.lower())
print(s1.title())
print(s1.swapcase())
print(s1.capitalize())# only one letter is the upper case rest of lower
print(s1.startswith('Python'))
print(s1.endswith('easy'))

# To print chracter at odd position and even position for the given strings
s= input("Enter the Strings")#using Slice operator
print("Charcter at even position:::",s[::2])
print("Charcter at odd position:::",s[1::2])
# without using Slice operator

i=0
print("the charcter at Even Position::::::")
while i<len(s):
    print(s[i],end="")
    i=i+2
print("the charcter at odd Position::::::")
i=1  
while i<len(s):
    print(s[i],end="")
    i=i+2

#################################
s=input("Enter the Strings:::::::::::")
s1=s2=output=''
for x in s:
    if x.isalpha():
        s1=s1+x
    else:
        s2=s2+x 
# print(s1)
# print(s2)
   
# for x in sorted(s1):
#     output=output+x           

# for x in sorted(s2):
#     output=output+x           
# print(output)
output=s1+s2
print(sorted(output))
# s=input("Enter the Strings::::::::::")
# output=''
# for x in s:
#     if x.isalpha():
#         output=output+x
#         previous=x  
#     else:
#        output=output+previous*(int(x)-1) 
# print(output)       



s=input("Enter the Strings::::::::::")
output=''
for x in s:
    if x.isalpha():
        output=output+x
        previous=x  
    else:
       newchar=chr(ord(previous)+int(x))
       output=output+newchar
print(output)        