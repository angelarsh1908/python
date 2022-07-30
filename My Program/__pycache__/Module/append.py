'''shopping_cart=[]

status = True
while status:   
    item=input("Enetr item")
    shopping_cart.append(item)
    choice=input("Do you want to add more item Y/N")
    if choice=='NO' or choice=='n' or choice=='no':
        status==False
        print("----------SHOPPING CART------------")
        print(f"you have added:={len(shopping_cart)}in your cart")
        for item in shopping_cart:
           print(item)'''

  
#add elemnet in existing list

shopping_cart=[]
for i in range(1,6):
    item=input("Enter item")
    shopping_cart.append(item)
    print(shopping_cart)