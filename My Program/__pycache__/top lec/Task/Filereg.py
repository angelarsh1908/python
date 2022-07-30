
from datetime import datetime
f= open("file1", 'w')
name=input("Enter your Name")
age=input("Enter your Age")
Gender=input("Enter your gender")
vaccine=input("Enter your complete dose")
f.write("Name"+name)
f.write("age"+age)
f.write("Gender"+Gender)
f.write("vaccinate"+vaccine)
current_datetime = datetime.now()
print("Current date & time : ", current_datetime)
str_current_datetime = str(current_datetime)
file1 = str_current_datetime+".txt"

print("File created : ", f.name)
#f=open("file_name","w")

f.close()
