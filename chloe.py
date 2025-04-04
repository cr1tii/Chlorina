import re
import random
from rich.console import Console

def chlorina():
    while True:
        l1 =[["hi", "hi", "nice to meet you","hi,im Chloe!"],["i want to know about chimstery", "sure! what do you want to know about?"], "chimestry", "ofc!", "sure i can help you!",["elements", "okay which one?","chlorine"],["chlorine", "i can help you whatever you like!.."]]
        int1 = input("chat with chloe : ")
        add = l1.pop(0)
        l2 = []
        l2.append(add)
        if re.search(l2[0][0],int1 ,re.IGNORECASE):
            print(random.choice(l2[0][1:3]))
        elif re.search(l2[0][0],int1,re.IGNORECASE) is None:
            l1.append(l2.pop(0))
            add2 = l1.pop(0)
            l2.append(add2)
            print(random.choice(l2[0][1:3]))
        elif int1 == "q":
            print("quiting...")
            return        
                
chlorina()

