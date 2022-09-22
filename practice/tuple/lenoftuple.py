tuplex = tuple("w3resource")
print(tuplex)
#use the len() function to known the length of tuple
print(len(tuplex))


x = ("w3resource")
# Reversed the tuple
y = reversed(x)
print(tuple(y))
#create another tuple

l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print([t[:-1] + (100,) for t in l])

L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
L = [t for t in L if t]
print(L)

l = [(1,2), (3,4), (8,9)]
print(list(zip(*l)))
