from ast import Num
from asyncio import events
import numbers


class pythonpro:
    def checkpositivrnagative(self,new):
        if new>=0:
             print("positive numbers")
        else:
             print("Nagative number")
    def findevenodd(self,new):
        if new%2==0:
            return "Even"
        else:
            return "odd"
pobj=pythonpro()
num=int(input("Enter a number"))
pobj.checkpositivrnagative(num)
print(pobj.findevenodd(num))

      
