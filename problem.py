s1=input("Enter First String")
s2=input("Enter Second Sttring")
output=''
i=j=0
while i<len(s1) or j<len(s2):
    # output=output+s1[i]+s2[j]
    # i=i+1
    # j=j+1
    if i<len(s1):
        output=output+s1[i]
        i=i+1
    if j<len(s2):
        output=output+s2[j]
        j=j+1

print(output)