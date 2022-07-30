'''from secrets import choice


def menu():
    data="""
                 MENU
            Press1 for addition 
            press2 for substraction
            press3 for division

         """
    print(data)
    choice=int(input("Enter your choice"))
    if choice==1:
      addition()
    elif choice==2:
     substraction()
    elif choice==3:
      division()
      pass
     

def addition():
    num1=int(input("Enter num1"))
    num2=int(input("Enter num2"))
    add=num1+num2
    print(add)
def substraction():
     num1=int(input("Enter num1"))
     num2=int(input("Enter num2"))
     sub=num1-num2
     print(sub)
def division():
     num1=int(input("Enter num1"))
     num2=int(input("Enter num2"))
     div=num1/num2

     print(div)
menu()'''
