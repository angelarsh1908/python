# f=open("mmfile1.txt","w")
# name=input("Enter name:")
# sub=input("Enter subject:")
# f.write("\n name"+name)
# f.write("\n name"+sub)
# f.close()

f=open("mmfile1.txt","w")
for i in range(1,5):
 name=input("Enter your name")
 f.write("\n name"+name)
f.close()