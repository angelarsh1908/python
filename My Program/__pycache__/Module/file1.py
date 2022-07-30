f=open("file2.txt","w")

f.write("my first file created by python")
f.write("Hello users")

'''name=input("Enter your Name")
subject=input("Enter your subject")
f.write("\n name="+name)
f.write("\n subject="+subject)
f.close()
'''

F=open("myfile.txt","a")
for i in range(1,6):
    name=input("Enter your name:")
    f.write("\n name="+name)
f.close()

