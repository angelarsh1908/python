#
from random import random


import random
print("----------------Welcome To IPL 2022------------------")

IPL_team=["CSK","MI","RCB","GT","RR"]
for team in IPL_team:
   print(team)
myteam=input("enter your team:")
print(myteam.upper())
IPL_team.remove(myteam)
print(myteam)
op_team=random.choice(IPL_team)
print("random select team:",op_team)

toss=["H","T"]
toss_value=random.choice(toss)
print("TOSS VALUE IS:",toss_value)
if toss=="H":
    print("myteam batting first",myteam) 
else:
    print(op_team)
super_over=[0,1,2,3,4,6,"OUT",0,1,2,3,4,6,"OUT"]
my_score=0
op_score=0
for i in range(1,7):
 my_score=random.choice(super_over)
 print(my_score)
 
 if my_score=="OUT":
    print("vicket")
    
    
    '''my_score=my_score+0
    print(my_score)'''

else:
   my_score=my_score+0
   print(my_score)

