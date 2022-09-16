# marks=[22,34,55,67]
# # percentage=((sum(marks)/400)*100)
# percentage=((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
# print(percentage)

def per(marks):
     p=((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
     return p

marks1=[22,34,55,67]
percentage1=per(marks1)

marks2=[11,22,33,44]
percentage2=per(marks2)

print(percentage1,percentage2)

def greet(name="Alka"):
    print("Good day ,"+name)

greet("Harsh")
greet()

def mysum(a,b):
    return(a+b)
h=mysum(2,2)
print(h)