# city=input("Enter Your City Name:::::::::::")
# list=["Hyd", "Delhi","Mumbai", "Banglore"]
# if city.strip() in list:
#     print("your City {} is available in your List".format(city))
# else:
#     print("Plz Enter Valid city")   
# No of occurence in string
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
print(s.replace("difficult","easy"))
