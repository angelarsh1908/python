# num=int(input("Enter the number"))

# for i in range(2,num):
#     if(num%2==0):
#         print("NOT PRIME")
#     else:
#         print("PRIME")

num=int(input("Enter the number"))
prime=True
for i in range(2,num):

    if(num%2==0):
        prime=False
        break
        
if prime:
    print(" PRIME")
else:
    print(" NoT PRIME")