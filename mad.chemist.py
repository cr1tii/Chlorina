from rich.console import Console
import time
cc = Console()
print("\n \n")
cc.print("   !!!!! mad chemist !!!!!!   ",style="bold red")
ask = input("\n hello there may i ask your name? : ")
print(f" nice to meet you {ask} ")
time.sleep(0.2)
print(" and not welcome in to my Lab, but i have to!, imagine this crazy guy CyberTale made me do this im too old for this!!!")
print("forget about it , i will let this guy know his limits")
print("im going out , i leave this Lab to you, try not to brun it! Lol")
print("\n \n")
print("1. start game")
print("2. tutorial")
print("3. exit")

def game():
    while True:
        madques = input("   : ")
        if madques == str(1):
            pass
        elif madques == str(2):
            bgmasg = """
            It is a simple game where some scientists from other rooms ask you to give them a specific element to complete their experiments. However, you don't have that element, so you may have to synthesize it manually.

            """
            cc.print("\n",bgmasg,"\n", style="bold")
            print("as an example im asking you to make me a 2kCl ")
            print(" what am i supposed to do? ,please take a one")
            cc.print("\n you can type 1 to quit", style="color(8)")
            madques2 = input("add K/Kr : ")
            if madques2 == "K":
                print("yes! , that was the right answer and it will give you k = 2K + Cl₂ → 2KCl")
                print("where if you picked the other itll be a wrong answer you knew now! have fun!")
                cc.print("you can type (1), to quit",style="color(8)")
            elif madques2 == "Kr":
                print("no! thats a wrong answer , Kr + Chlorine will give you Kr =  Kr + Cl₂ → KrCl₂")
            elif madques2 == str(1):
                break
        elif madques == str(3):
            break
game()
