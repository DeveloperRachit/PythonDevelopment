List=[2,5,8,6,2,1]  #we can use anyLIST here
                                   #(eg) range(0,9,2)
                                   #(eg) [1,2,'s','r',3+9j]
print('FOR in sequence [BY USING WHILE]\n')

l,n=len(List),0     #{head
while(n<l):           #
    i=List[n]               #}
    print(i)                 #body of the loop
    n+=1                    #{foot}

print('\n--------------------------------')
print('FOR in sequence [BY USING FOR  ]\n')

for i in List:         #{head}
    print(i)                #body of the loop
                             #no foot required
