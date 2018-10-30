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