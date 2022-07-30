'''num1="45"
print(type(num1))
num2=int(num1)
print(type(num2))
num3=45
num4=str(num3)
print(type(num4))
num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2 :"))
print(num1+num2)
#print(type(num2))'''

#if Statement

'''age=int(input("Enter yuor age"))
if age>=18:
    print(age)

#if.... else Statement

age=int(input("Enter your age"))
if age>=18:  
   print("You are not eligible")
else :
   print("You are bellow 18")

no=int(input("Enter your number"))
if  no%2==0:
    print("Positive number")
else:
    print ("Nagative number")  

#Nested If....

day=int(input("Enter your number"))
if day==1:
    print("monday")
elif day==2:
    print("Tuesday")
elif day==3:
    print("Wednesday")
elif day==4:
    print("Thursday") 
else:
    print("invalid Statement")  '''

CSK=int(input("Enter CSK score")) 
MI=int(input("Enter MI Score"))
RCB=int(input("Enter RCB Score"))
if MI>RCB:
    if MI>CSK:
        print("MI won the Match")
    else:
        print("CSK Won the MAtch")
else:
    if RCB>CSK :
        print("RCB Won the Match")
    else:
        print("CSK won the match")

              

   







    

