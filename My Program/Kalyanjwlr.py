#Kalyan Jewellers
Making_charges=2500
fname=(input("Enter your First Name"))
lname=(input("Enetr your Last Name"))

gen=int(input("Enter your gender 1 for female and 2 male"))
if gen==1:
   print("female")
else:
   print("male")
age=int(input("Enter your age"))
if age>60:
    print("Seniour Citizen")
Vac_status=int(input("Enetr Number 1 if you are vaccinated"))
if Vac_status==1:
    print("You Are Vaccinated!")
else :
   print("You Are not Vaccinated!")

puramount=int(input("Enter your Amount"))

#if gen==4 and age>60 and puramount<100000:

if gen==2 and age>60 and puramount>100000:
     per_cm1=puramount*0.15
     a=puramount-per_cm1
     print(a)
     print("final Price with making charges= ",Making_charges+a)
     print("-------------INVOICE-----------------")
     print("FIRSTNAME/t:",fname) 
     print("LASTNAME",lname)
     print("GENDER",gen)   
     print("AGE",age)
     print("PURCHASE AMOUNT",puramount)
     print("MAKING CHARGES",Making_charges)
     print("DISCOUNT :30% Discount on Amount")
     
     
elif gen==2 and age>60 and puramount>200000:
     per_cm2=puramount*0.25
     b=puramount-per_cm2
     print(b)
     print("final Price with making charges= ",Making_charges+b)
elif gen==2 and age>60 and puramount>300000:
     per_cm3=puramount*0.35
     c=puramount-per_cm3
     print(c)
     print("final Price with making charges= ",Making_charges+c)

elif gen==1 and age>60 and puramount>100000:
     per_cf1=puramount*0.20
     d=puramount-per_cf1
     print(d)
     print("final Price with making charges= ",Making_charges+d)
elif gen==1 and age>60 and puramount>200000:
     per_cf2=puramount*0.30
     e=puramount-per_cf2
     print(e)
elif gen==1 and age>60 and puramount>300000:
     per_cf3=puramount*0.40
     f=puramount-per_cf3
     print(f)
     print("final Price with making charges= ",Making_charges+f)
     
     

elif gen==1 and age<60 and puramount>100000:
     per_cfy1=puramount*0.15
     g=puramount-per_cfy1
     print(g)
     print("final Price with making charges= ",Making_charges+g)
elif gen==1 and age<60 and puramount>200000:
     per_cfy2=puramount*0.25
     h=puramount-per_cfy2
     print(h)
     print("final Price with making charges= ",Making_charges+h)
     print("-------------INVOICE-----------------")
     print("FIRSTNAME/t:",fname) 
     print("LASTNAME",lname)
     print("GENDER",gen)   
     print("AGE",age)
     print("PURCHASE AMOUNT",puramount)
     print("MAKING CHARGES",Making_charges)
     print("DISCOUNT :30% Discount on Amount")
     
elif gen==1 and age<60 and puramount>300000:
     per_cfy3=puramount*0.35
     i=puramount-per_cfy3
     print(i)
     print("final Price with making charges= ",Making_charges+i)
     print("-------------INVOICE-----------------")
     print("FIRSTNAME/t:",fname) 
     print("LASTNAME",lname)
     print("GENDER",gen)   
     print("AGE",age)
     print("PURCHASE AMOUNT",puramount)
     print("MAKING CHARGES",Making_charges)
     print("DISCOUNT :30% Discount on Amount")
    
elif gen==2 and age<60 and puramount>100000:
     per_cmy1=puramount*0.10
     j=puramount-per_cmy1
     print(j)
     print("final Price with making charges= ",Making_charges+j)
     print("-------------INVOICE-----------------")
     print("FIRSTNAME/t:",fname) 
     print("LASTNAME",lname)
     print("GENDER",gen)   
     print("AGE",age)
     print("PURCHASE AMOUNT",puramount)
     print("MAKING CHARGES",Making_charges)
     print("DISCOUNT :30% Discount on Amount")
     print("With Discoubt",l)
elif gen==2 and age<60 and puramount>200000:
     per_cmy2=puramount*0.20
     k=puramount-per_cmy2
     print(k)
     print("final Price with making charges= ",Making_charges+k)
     print("-------------INVOICE-----------------")
     print("FIRSTNAME/t:",fname) 
     print("LASTNAME",lname)
     print("GENDER",gen)   
     print("AGE",age)
     print("PURCHASE AMOUNT",puramount)
     print("MAKING CHARGES",Making_charges)
     print("DISCOUNT :30% Discount on Amount")
     print("With Discoubt",l)
elif gen==2 and age<60 and puramount>300000:
     per_cmy3=puramount*0.30
     l=puramount-per_cmy3
     print(l)
     print("final Price with making charges= ",Making_charges+l)
     #m=l+2500
     #print(m)
     #l=int(input("Total Amount + 2500 making charges",l+2500))
     print("-------------INVOICE-----------------")
     print("FIRSTNAME/t:",fname) 
     print("LASTNAME",lname)
     print("GENDER",gen)   
     print("AGE",age)
     print("PURCHASE AMOUNT",puramount)
     print("MAKING CHARGES",Making_charges)
     print("DISCOUNT :30% Discount on Amount")
     print("With Discoubt",l)
 

else:
     ("Discount not applied")





   





