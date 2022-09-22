list=[2,2,3,3,45,55,55,4]
l1=[]
for item in list:
    if item not in l1:
        l1.append(item)
print(l1)


def dup(list):
    l1=[]
    for item in list:
        if item not in l1:
            l1.append(item)
    return l1
list=[2,2,3,3,45,55,55,4]
print(l1)

list=[2,2,3,3,45,55,55,4]
print(set(list))      
