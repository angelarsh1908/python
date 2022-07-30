#for i in range(1,6):
#for i in range(1,6):
#   print(i,"hello")

'''firsname="ALka"
subject="Python"
print("hello",firsname,"Your subject is python")
print(f"hello {firsname} Your {subject} is python")'''

#for i in range(1,6):
 #   print(f"({i}) Hello")
 
'''for i in range(1,6):
    num=int(input("Enter Number"))
    if num%2==0:
        print("positive")
    else:
        print("nagetive")'''

'''for num in range(1,6):
    num=int(input("Enter num"))
    sum=sum+num
    print(sum)'''

import random
computer_guess=random.randint(1,100)
for i in range(1,6):
    user_guess=int(input("Enter number"))
    print(user_guess)
    if user_guess>computer_guess:
     print("HINT:Lower Number")     
    elif user_guess<computer_guess:
        print("HINT:Higher number")
    else:
        print("You win!!!")
print("computer_guess=",computer_guess)