import time
import random
import pyfiglet
from rich.console import Console
from Elist import Lis
from ElistDic import Les
#note class in the start
class att:
  def __init__(self, at1):
    self.at1 = at1
  def as1(self):
    self.at1()
  @staticmethod
  def as1dorun():
    c1 = Console()
    x0 = pyfiglet.figlet_format("SA6",font="big")
    c1.print(x0,style="pink1")
    c1.print("\nwelcome to SA6.")
    c1.print("\n powered by CyberTale. ",style="color(8)")
def sf():
  print('simple sf')

e1 = att(sf)
att.as1dorun() # the end of note class

# list menu loop
while True:
  print(f"-"*36)
  print('\n\n')
  print('type:')
  print('1. elements house')
  print('2. for showing the periodic table of elements ')
  print('3. for chlorine actions with elements')
  print('4. to defintion of chlorine ')
  print('5. about the app')
  print('6. to exit')
  print("\n\n\n")
  print(' ask what you like sir?')
  
  #i1 list table

  int1 = input(' : ')
  my_list = Les()
  # 1 command in list menu
  if int1 == '1':
    while True:
        console = Console()
        console.print("welcome to elements house!\n",style=" bold color(94)")
        console.print("1. search element.",style="color(94)")
        console.print("2. more informations about the elements ",style="color(94)")
        console.print("\n  (just to know in this part of menus you can alsways type q to exit)\n",style="color(15) bold")
        console.print("type what you want:",style="bold color(94)",end=" ")
        input1 = input()
        time.sleep(0.0)
        if input1 == str(1):
            while True:
                console.print("\n1. regular search.",style="color(91)")
                console.print("2. specific search.",style="color(91)")
                console.print("3. search by type.",style="color(91)")
                print("\n")
                console.print(" try:",end=" ",style="color(94)")
                inp5 = input()
                if inp5 == str(1):
                    while True:
                        print("\n")
                        console.print("search!:",end=" ",style="color(94)")
                        inp1 = input()
                        k1 = my_list.sbnos(inp1)
                        console.print("\n",k1,"\n",style="color(94)")
                        if inp1 == 'q':
                            break
                elif inp5 == str(2):
                    while True:
                        print("\n")
                        console.print("search symbol!: ",end=" ",style="color(94)")
                        inp6 = input()
                        k2 = my_list.getsymbol(inp6)
                        console.print("\n",k2,"\n",style="bold color(94)")
                        if inp6 == 'q':
                            break
                elif inp5 == str(3):
                    while True:
                        console.print("search  Type!:",end=" ",style="bold color(94)")
                        inp8 = input()
                        k3 = my_list.FilterType(inp8)
                        console.print("\n",k3,"\n",style="bold color(94)")
                        if inp8 == 'q':
                            break
                if inp5 == 'q':
                    break
        elif input1 == str(2):
            def summon():
                print('\n\n')
                from infoData import main
                main()
            summon()            
        elif input1 == 'q':
            break
        else: 
            console.print(f"\n  symbol not found!.",style="bold red")
  # 2 command in list menu
  elif int1 == '2':
    print("increasing...")
    time.sleep(0.5)
    #i2 summoning table
    mylist = Lis()
    ll1 = mylist.ele()
    ll2 = mylist.eleNames()
    for l1 ,l2 in zip(ll1,ll2):
      c1 = Console()
      c1.print(l1,":",l2,style="bold blue")  # i3 command in list menu
  elif int1 == '3':
    c1 = Console()
    #3 showing up table
    c1.print(" #i added all the elements , no need to see the entire list just type whatever you want",style="red")
    c1.print("\n here's a simple ex to help you to get chlorine actions with the p.e list", style='bold red')
    c1.print("\n H + Cl:",style="bold red")
    c1.print('\n H₂ + Cl₂ → 2HCl',style='bold underline yellow')

    print(f"—"*38)
    print('\n1. print1 for a 1 + 1 simple calcuate')
    print('2. print2 to exit 3')
    in1 = input(': ')
    if in1 == '1':
      class rea1:
        def __init__(self):
          pass
        def asrea(self):
          while True:
            inp1 = input("\ntype a symbol (or type 1 to quit): ")
            c1 = Console()
            #i3 actions table
            rea = mylist.eleAct()
            reaction = rea.get(inp1,"symbol not found")
            c1.print(f"\n",reaction,style="bold underline yellow")
            if inp1 == '1':
              break
            else:
              continue
      @staticmethod
      def asrea1():
        pass
      @staticmethod
      def asrea2():
        pass

      roa = rea1()
      roa.asrea()
  # 4 command in list menu
  elif int1 == '4':
      print("\n")
      msg = """
      Chlorine is a chemical element with the symbol Cl and atomic number 17. It belongs to the halogen group in the periodic table and is a yellow-green gas with a strong, pungent odor. It is used for water disinfection, the production of plastics like PVC, and various chemical industries.
      """
      cc = Console()
      cc.print(msg, style="bold")
      print("\n")

      # Ai task
      # ...

  elif int1 == "5": #task 5
      c1 = Console()
      msg = """
    This is a simple application that simulates an environment where random elements react with chlorine.\n\n it cost me too much time to finish this code because i was busy and i had too much unreleased functions that had to delete them, even tho i finished the original version once but imagine i accidentally deleted it.  yeah , so i had this old , one of my unreleased files as well.\n first SA7 had to be droppen but i had issues so i replaced with SA6, i had issues in SA6 too so i replaced with 0SA6, finished 0SA6 and accidentally deleted mow came back to edit on SA6 again and finish it as well.\n\n\n HOW TO USE SA6 FUNCTIONS? :\n well here some explanations on how you run this code.\n first you got func 1 where you search an element , either more elements based on letter like elements thats start with letter A you type A and search in regular search , you want a specific search you choose specific, all the inputs you can quiet them as well by typing q.\n you got also where you search types of elements either you want more informations you go back and type 2 for more infos.\n func 2 you see the names or the elements of the table.\n  for 3 if you want an specific equation of an elements just type the one you want.\n for 4 you see the defntion of the chlorine wich of the chlorine wich is why i wrote this whole code.\n 5 as well its the infos that are based here.\n 6 to queit the code.\n\n —— if there bugs i will fix it later and drop as a re-release to 0SA6. no words for SA7 untill another notice.—— 
    """
      c1.print(msg, style="bold pink1")
      c1.print(f"\nyou can type .2 to view the table that are exists in the list",style="bold pink1")
      c1.print("\n featured(Ai, )",style="color(8)")
  elif int1 == "6": #6 task
      break
  else:
      c1 = Console()
      c1.print(f"error, please right a word from the list.",style="bold red")
