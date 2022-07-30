#x=lambda a:a+a
#print(x(10))

def addition(*num):
    sum=0
    for i in num:
        sum+=i
    print(sum)
addition(2,2,3,4,5,6,7)

def student(**d):
 student(name="aaaa",subject="ddf")