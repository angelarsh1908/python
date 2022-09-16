mydict={
    'pankha':'fan',
    "Dabba":'bax',
    'vastu':'item',
}
print('option are',mydict.keys())
a=input('enter the value :')
#print("The meaning of tour word is :",mydict[a]) #error
print("The meaning of tour word is :",mydict.get(a))