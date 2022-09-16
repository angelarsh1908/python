import random

def gamewin(comp ,you):
    if comp == you:
        return None
    if comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    if comp == 'w':
        if you=='g':
            return False
        elif you =='s':
            return True
    if comp =='g':
        if you =='s':
            return False
        elif you =='w':
            return True
            
            
print("Comp Turn: Snake(s) or Water(w) or gun(g)?")
randno=random.randint(1,3)
if randno==1:
     comp = 's'
elif random==2:
     comp ='w'
elif randno==3:
     comp = 'g'

you=input("Your Turn: Snake(s) or Water(w) or gun(g)?")
a = gamewin(comp ,you)

print(f"computer choose {comp}")
print(f"you choose {you}")

if a == None:
    print("The game is tie")
elif a:
    print("you win")
else:
    print("You loose")