print("----------------------Linear Housie--------------------")

from asyncio.windows_events import NULL
import random 
main_list=[]
for i in range(0,12):
    r=random.randint(1,100)
    if r not in main_list:
     main_list.append(r)
print(main_list)

main_ticket = main_list
print()

print("Welcome!!! Select your number Randomly")
'''random.shuffle(main_ticket)
print(main_ticket)'''

print()
#slicin
player1=main_list[:6]
print("Player1=",player1)
player2=main_list[ 6:]
print("Player2=",player2)

status=True
while status:

  ticket = random.choice(main_ticket)
  print(ticket)
  if ticket in player1:
       player1.remove(ticket)
       main_ticket.remove(ticket)
       print("Player1=",player1)
       print("player2=",player2)
       if player1==[]:
               print("\t\tPlayer1 is win!!!")
               break
       
         
  elif ticket in player2:
       player2.remove(ticket)
       main_ticket.remove(ticket)
       print("Player1=",player1)
       print("Player2=",player2)
      
       if player2==[]:
            print("\t\tPlayer2 is win!!!")
            break
  else:
      status=False
    






