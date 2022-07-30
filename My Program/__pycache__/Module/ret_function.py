#def greeting(a):
#    print(a,"Hello Good Morning")
#a=greeting("H")

#def sum(num1,num2):
#    ans=num1+num2
#    print(ans)
#
#sum(11,2)

from mailbox import NoSuchMailboxError


def menu():
    data="""
         press1 for factorial
         press2 for even or odd
         """
    print(data)
    choice=int(input("enter your choice"))
    if choice==1:
        num=int(input("Enter your number"))
        print(factorial(num))
    elif choice==2:
        num=int(input("Enter your number"))
        print(checkoddeven(num))
    else:
        print("Invalid Number")

def factorial(number):
    #5*4*3*2*1
    f=1
    for i in range(1,number+1):
        f*=i
    return f
def checkoddeven(number):
   if number%2==0:
       return "even number"
   else:
       return "Odd number"

menu()


