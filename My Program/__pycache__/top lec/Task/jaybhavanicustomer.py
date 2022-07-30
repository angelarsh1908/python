from site import venv


print("=========================MENU==========================")
cust_product={

  
     1:{
         "pro":"Vadapav",
         "price":30, 
         "qty":5,         
       },
     2:{
           "pro":"Dabeli",
           "price":25,
           "qty":5, 
      },
      3:
      {
          "pro":"Bhel",
          "price":50,
          "qty":5, 
      },
      4:
      {
          "pro":"Pavbhaji",
          "price":70,
          "qty":5, 

      },
      5:{
          "pro":"Pulav",
          "price":70,
          "qty":5, 
      }

    }
for i in range(1,5):

    for k,v in cust_product[i].items():
        if k=="qty":
            continue
        else:
           print(f"{k}.................{v}")

prod=input("Enter your Product:")
qtiy=input("enter your quantity:")

prod=cust_product["pro"]
if prod==1:
    




      
