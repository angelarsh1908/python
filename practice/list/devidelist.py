myList = [10,20,30,40,50,60,70,80,90]
myInt = 10
newList = [x / myInt for x in myList]
print(newList)

li = [38, 57, 76, 95, 114, 161.5]
num = 19
res = []
for val in li:
    res.append(val/num)
print(res)

li = [38, 57, 76, 95, 114, 161.5]
num = 19
res = list(map(lambda x: x/num, li))
print(res)

name = 'abcdef'
suffix = [1,2,3,4,5,6]
zip(name, suffix)
