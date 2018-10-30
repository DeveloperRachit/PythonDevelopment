s=input("enter the string:::::::")  
if (len(s))<2:
    print(s) 

result = []
for i in s:
    if i not in result:
        result.append(i)

print(''.join(result))
# removeDuplicate("missippi")    