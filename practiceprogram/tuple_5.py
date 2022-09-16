# t=(3,4,45,66,78,9,0,3,3)
# print(t.count(3))
# print(t.index(45))
# myDictionary={

# myDict={
#     "alka":"she is a good girl",
#     "subject":"python",
#     "marks":[1,2,3], #valid
#     "anotherdict":{ 'harry':'player'},
#      1:2
# }
# print(myDict['alka'])
# print(myDict['subject'])
# myDict['marks']=[44,45]
# print(myDict['marks']) 
# print(myDict['anotherdict'])


myDict={
     "alka":"she is a good girl",
     "subject":"python",
     "marks":[1,2,3], #valid
     "anotherdict":{ 'harry':'player'},
     1:2
 }
# print(myDict.keys())
# print(type(myDict))
# print(list(myDict.keys()))
# print(list(myDict.values()))
# print(list(myDict.items())) #all content of dict    
print(myDict)
updatedict={
    'lavish':'alka',
    'subject':"english"
}
myDict.update(updatedict)
print(myDict)
print(myDict.get("Alka"))#nune return
print 
