#creating blank list ""
#shopping_list=[]
#print(shopping_list)

'''shopping_list=["fruits","Vegetable","bread","Milk"]
#print(shopping_list)
for i in shopping_list:
    print(i)'''
 
subject_marks=[55,66,77,77,88]
for marks in subject_marks:
    #print(marks)
    '''
    print(f"maximum marks={max(subject_marks)}")
    print(f"minimum marks={min(subject_marks)}")
    print(f"total marks={sum(subject_marks)}")
    '''
    #print(len(subject_marks))
    #subject_marks.sort()
   # print(subject_marks)
    subject_marks.sort(reverse=True)
    print(subject_marks)
    break


 #for j in range(6):
'''r1=random.choices(list,k=6)
print("Player1=",r1)
rl1=random.choice(list)
if rl1 not in r1:
   print(r1)
   status=True
   while status:
    rl1=random.choice(list)
    print(rl1)
    list.remove(rl1)
    print("Player1=",rl1)
else:
   r2=random.choices(list,k=6)
   print("player2=",r2)
   rl2=random.choice(r2)
   print(r2)
   status=True
   while status:
    rl2=random.choice(r2)
    print(rl2)
    r1.remove(rl2)
    print("Player2=",r2)'''



'''r2=random.choices(list,k=6)
print("player2=",r2)
rl2=random.choice(r2)
print(rl2)'''