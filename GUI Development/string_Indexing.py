name ="python"
# p=0
# y 1
# t 2
# h 3
# o 4
# n 5

print(name[2])

#slicing()/ selecting sub sequence
#syntax -[start arg : stop arg-1]
print(name[0:2]) #if have to print till y then need to write 2
print(name[2:4])
print(name[2:])
print(name[:3]) 


print("rachit" [0:5:2]) #step arguments
print("rachit"[0::3])
print("rachit"[5::-1]) # string reverse

print("rachit"[::-1])

# reverse a string in 2 line
name=input("enter the name")
print(f"reverse of string is {name[-1::-1]}")