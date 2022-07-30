'''shopping_cart=[]
for i in range(1,6):
    item=input("Enter item")
    shopping_cart.append(item)
print(shopping_cart)'''

#from secrets import choice
'''

shopping_cart=[]
status=True

while status:
    item=input("Enetr item")
    shopping_cart.append(item)
    choice=input("Do you want to add more item Y/N:")
    if choice=="n" or choice=="No" or choice=="N":
        status=False
print(shopping_cart)
for item in shopping_cart:
    print(item)'''

'''l1=[12,12,13,14]
l2=[101,102,103]
l1.extend(l2)
print(l1)'''

'''shopping_cart=["Fruits","veges","Medicines"]
shopping_cart.insert(1,"Mangoes")
print(shopping_cart)
shopping_cart.remove("Mangoes")
print(shopping_cart)

shopping_cart.pop()
print(shopping_cart)

shopping_cart.clear()
print(shopping_cart)

del shopping_cart
print(shopping_cart)
'''
'''import random
shopping_cart=["Fruits","veges","Medicines","Milk"]
random.shuffle(shopping_cart)
print(shopping_cart)'''

import random
 
data = ["samsung", "tata", "amazon", "flipkart", "mi"]
 
print(random.choice(data))

'''l1=[]
for item in shopping_cart:
    if item not in l1:
        l1.append(item)
        print(l1)'''



