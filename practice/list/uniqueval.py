list=[3,4,5,6,7,8,8]
# a=set(list)
# a=list
# print(a)

l1=[]
for item in list:
    if item not in l1:
        l1.append(item)
print(l1)
