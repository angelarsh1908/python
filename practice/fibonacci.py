a=0
b=1
# num=int(input("Enter number"))
for i in range(0,100):
    c=b
    b=a
    a=c+b
    print(a)