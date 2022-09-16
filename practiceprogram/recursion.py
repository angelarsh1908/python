def fact_iter(n):
    product=1
    for i in range(n):
        product=product*(i+1)
    return(product)

f=fact_iter(5)
print(f)

def fact_recursion(n):
    if n==1 or n==0:
        return 1
    else:
        return n * fact_recursion(n-1)
print(fact_recursion(5))



