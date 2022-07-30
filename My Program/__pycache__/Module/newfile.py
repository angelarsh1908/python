"""
r=read
w=write
a=append
x=create new file
"""
f=open("myfile.txt","w")
'''#print(f.readline())
l1=f.readline()

print(l1)'''
f.write("My First File created by python")
f.write("Hello users")
f.close()
