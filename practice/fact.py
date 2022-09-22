num=int(input("Enter number"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))