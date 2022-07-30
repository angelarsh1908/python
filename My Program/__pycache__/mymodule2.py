import mymodule
num1=int(input("num1="))

num2=int(input("num2="))
print(mymodule.sum(num1,num2))

from mymodule import mul

print(mul(2,3))