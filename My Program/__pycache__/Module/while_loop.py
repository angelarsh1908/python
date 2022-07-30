'''ticket=5
while ticket>0:
    print("INSIDE THE GAME")
    ticket=ticket-1'''

#Example-2
'''status=True
while status:
  num=int(input("Enter a number"))
  if num%2==0:
      print("even number")
  else:
      print("odd number")
  choice=int(input("Do you want to add more number press 1 for 'Yes' and press 2 for no:"))
  if choice==1:
     status=True
  else:
     status=False'''

#Example-3 Game
'''status= True
sum=0

while status:
    num=int(input("Enter a number"))
    sum += num
    choise=input("Do you want to add more number:Y/N")
    if choise=='n' or choise=='no' or choise=='N' :
        status=False
        print("total sum=",sum)'''

#Example-4 computer guess

'''import random
computer_guess = random.randint(1,100)

status=True
while status:
    user_guess=int(input("Enet a random number"))
    if user_guess>computer_guess:
        print("HINT: Guess Lower Number")
    elif user_guess<computer_guess:
        print("HINT:Guess Higher Number")
    else :
        print("You win!!!")
        status=False'''
       
#Example-5 5 chance for user using for loop

'''import random
computer_guess=random.randint(1,100)

for i in range(1,6):
    user_guess=int(input("Enter random number"))
    if user_guess>computer_guess:
        print("HINT:Guess lower number")
    elif user_guess<computer_guess:
        print("HINT:Guess Higher Number")
    else:
        print("You win!!!")
    #break
else :
    ("game Over")'''

 






