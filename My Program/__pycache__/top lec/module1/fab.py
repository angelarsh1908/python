'''ticket=5
while ticket>0:
    print("Inside the Game")
    ticket=ticket-1'''

'''status=True
while status:
    num=int(input("Enter a number"))
    if num%2==0:
        print("Even number")
    else:
        print("odd number")    
    choice=int(input("add more number press 1 and press 2 for no:"))
    if choice==1:
            status=True
    else:
            status=False'''

'''status=True
sum=0
#baki
while status:
    num=int(input("enter a mumber"))
    sum+=num
    choice=input("Enter a more number")
    if choice=="n" or choice=="N" or choice=="NO":
      status==False
print(sum)'''

'''import random

computer_guess=random.randint(1,100)
for i in range(1,6):
    user_guess=int(input("Enter a number"))
    if user_guess>computer_guess:
        print("HINT:Guess Lower Number")
    elif user_guess<computer_guess:
        print("HINT:Guess Higher Number")
    else:
       print("GAME OVER")
       break
else:
    print(computer_guess)
'''

'''shopping_list=["mangos","banana","apple","bread"]
for item in shopping_list:
  print(item, end="  ")'''
'''
subject_marks=[45,66,77,87,98,8]
for marks in subject_marks:
  print(marks)
print(f"maximum marks={max(subject_marks)}")
print(f"minimum marks={min(subject_marks)}")
print(f"sum of marks={sum(subject_marks)}")'''

shopping_cart=[]
for i in range(1,6):
    item=input("Enter here")
    shopping_cart.append(item)
    print(shopping_cart)


