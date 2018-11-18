# printing elements in sorted way
t=(30,40,20,10,5,11,9,7,8)
# print(sorted(t))
# we have to methods for sorting Sorted (list) for tuples

l=sorted(t)
print("Tuple:", t)
# after sorrting that will return list object
print("List:", l)
t2=tuple(sorted(t))
print("Tuple::after :",t2)
t2=tuple(sorted(t,reverse=True))
print("Tuple::after reverse:",t2)
print(min(t2))
print(max(t2))