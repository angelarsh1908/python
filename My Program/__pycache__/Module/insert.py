#insert:to add element to specific position(index)
'''shopping_cart=["veges","fruits","Milk","medicines"]
shopping_cart.insert(1,"mango")
print(shopping_cart)'''

#-------------Remove-------------

#remove:remove specific elemene from existing List

#shopping_cart=["veges","fruits","Milk","medicines","Mangos","Milk","Mangos"]
'''shopping_cart.remove("Mangos")
print(shopping_cart)
shopping_cart.pop()
print(shopping_cart)
shopping_cart.clear()
print(shopping_cart)'
del shopping_cart
print(shopping_cart)'''

#shopping_cart=["Apple","Mangos","Banana","Kiwi","Mangos","Kiwi"]

'''shopping_cart=[]
for i in range(1,6):
    item=input("Enter item")
    shopping_cart.append(item)
print(shopping_cart)'''


'''shopping_cart=[]
status=True
while status:
    item=input("Enter Item")
    shopping_cart.append(item)

    choice=input("Do you want to add more item Y/N")
    if choice=='n' or choice=="No" or choice=='N':
        status=False
        print("-----------------SHOPPPING CART-----------------")
        print(f"\n You havev Added {len(shopping_cart)}item in shopping cart")
        for item in shopping_cart:
          print(item)'''

'''l1=[11,12,13]
l2=[11,11,11]
l1.extend(l2)
print(l1)'''

'''shopping_cart=["Apple","Mangos","Banana","Kiwi","Mangos","Kiwi"]
shopping_cart.insert(1,"Milk")
print(shopping_cart)'''

#remove elemnets from the list
from ast import Not


shopping_cart=["Apple","Mangos","Banana","Kiwi","Mangos","Kiwi"]
#shopping_cart.remove("Mangos")
#shopping_cart.pop()
#print(shopping_cart)
#shopping_cart.pop()
#shopping_cart.clear()
#del shopping_cart
#print(shopping_cart)
#print(shopping_cart.index("Banana"))
l1=[]
for item in shopping_cart:
    if item not in l1:
        l1.append(item)
print(l1)
