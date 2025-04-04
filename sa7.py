import time
import random
from rich.console import Console
#note class in the start
class att:
  def __init__(self, at1):
    self.at1 = at1
  def as1(self):
    self.at1()
  @staticmethod
  def as1dorun():
    c1 = Console()
    c1.print(f"attention",style="bold underline red on black")
    msg = """
    This is a simple application that simulates an environment where random elements react with chlorine.
    """
    c1.print(msg, style="bold pink1")
    c1.print(f"\nyou can type .i2 to view the table that are exists in the list",style="bold pink1")
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
  print('1. *i1* for typing symbol elements')
  print('1. *i2* for showing the periodic table of elements ')
  print('3. *i3* for chlorine actions with elements')
  print('4. *i4* to defintion of chlorine ')
  print('5. *i5* Ask Ai.')
  print('6. *i6* play games.')
  print('7. *i7* to exit')
  print("\n\n\n")
  print(' ask what you like sir?')
  
  #i1 list table

  list1 = ["H", "N", "O", "F", "Cl", "He", "Ne", "Kr", "Xe", "Rn", "Na", "K", "Ca", "Fe", "Al", "Cu", "Zn", "Mg", "p","S","C","Si", "B","Sn","Pb", "Ti", "Ag"]
  list2 = ['*hydrogen*', '*Nitrogen*', '*oxygen*', '*Flourine*', '*Chlorine*', '*Helium*','*Neon*','*Kryton*','*Xenon*','*Radon*','*Sodium*','*Potassium*','*Calcium*','*Iron*','*Aluminum*','*Copper*','*Zinc*','*Magnesium*','*Phosphorus*','*Sulfur*','*Carbon*','*Silicon*','*Boron*','*Tin*','*Lead*','*Titanium*','*Silver*' ]
  int1 = input(' : ')
  # i1 command in list menu
  if int1 == 'i1':
    while True:
      console = Console()
      console.print(f"\n(type 1 to exit if you want.)",style="bold underline cyan"      )
      input1 = input('  wirte the elemnt short from what you want:  ')
      syn = dict(zip(list1, list2))
      if input1 in syn:
        print('icreasing...')
        time.sleep(0.0)
        console.print(f"\nthe elemnt for {input1}, is {syn[input1]}!",style="bold yellow")
        time.sleep(0.0)
      elif input1 == '1':
          break
      else:
          console.print(f"\n  symbol not found!.",style="bold red")
          console.print(f"  check i2 to see the elements that exists in the list",style="bold red")
  # i2 command in list menu
  elif int1 == 'i2':
    print("increasing...")
    time.sleep(0.5)
    #i2 summoning table
    ll1 = ["H", "N", "O", "F", "Cl", "He", "Ne", "Kr", "Xe", "Rn","Na", "K", "Ca", "Fe", "Al", "Cu", "Zn", "Mg", "p","S","C","Si", "B",    "Sn","Pb", "Ti", "Ag"]
    ll2 = ['hydrogen','Nitrogen','oxygen', 'Flourine','chlorine','Helium','Neon','Kryton','Xenon','Radon','Sodium','Potassium','Calcium','Iron','Aluminum','Copper','*Zinc','Magnesium','Phosphorus','Sulfur','Carbon','Silicon',    'Boron','Tin','Lead','Titanium','Silver' ]
    for l1 ,l2 in zip(ll1,ll2):
      c1 = Console()
      c1.print(l1,":",l2,style="bold blue")  # i3 command in list menu
  elif int1 == 'i3':
    c1 = Console()
    #i3 showing up table
    realist = ['H','O','F','Og', 'Ar','Na','Kr','Xe','Rn',"Na", "K", "Ca", "Fe", "Al", "Cu", "Zn", "Mg", "p","S","C","Si", "B",        "Sn","Pb", "Ti", "Ag"]
    c1.print(realist,style="bold red")
    c1.print("\n here's a simple ex sir to help you to get chlorine actions with the p.e list", style='bold red')
    c1.print("\n H + Cl:",style="bold red")
    c1.print('\n H₂ + Cl₂ → 2HCl',style='bold underline yellow')

    print(f"—"*38)
    print('\n1. print1 for a 1 + 1 simple calcuate')
    print('2. print2 to exit i3')
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
            rea = {
          "H": "H₂ + Cl₂ → 2HCl",
          "N": "N₂ + 3 Cl₂ → 2 NCl₃",
          "O": "O₂ + 2 Cl₂ → 2 OCl₂",
          "F": "F₂ + Cl₂ → 2 ClF",
          "Og": "Og + Cl₂ → OgCl₂",
          "Ar": "Ar + Cl₂ →no reaction",
          "Na": "2Na + Cl₂ → 2NaCl",
          "Kr": "Kr + Cl₂ → KrCl₂",
          "Xe": "Xe + Cl₂ → XeCl₂",
          "Rn": "Rn + Cl₂ → RnCl₂",
          "Na": "2Na + Cl₂ → 2NaCl",
          "k" : "2K + Cl₂ → 2KCl",
          "Ca": "Ca + Cl₂ → CaCl₂",
          "Fe": "2Fe + 3Cl₂ → 2FeCl₃",
          "Al": "2Al + 3Cl₂ → 2AlCl₃",
          "Cu": "Cu + Cl₂ → CuCl₂",
          "Zn": "Zn + Cl₂ → ZnCl₂",
          "Mg": "Mg + Cl₂ → MgCl₂",
          "P" : "2P + 5Cl₂ → 2PCl₅",
          "S" : "S + Cl₂ → SCl₂ (or S₂Cl₂)",
          "C" : "C + 2Cl₂ → CCl₄",
          "Si": "Si + 2Cl₂ → SiCl₄",
          "B" : "2B + 3Cl₂ → 2BCl₃",
          "Sn": "Sn + 2Cl₂ → SnCl₄",
          "Pb": "Pb + Cl₂ → PbCl₂",
          "Ti": "Ti + 2Cl₂ → TiCl₄",
          "Ag": "2Ag + Cl₂ → 2AgCl",
      }
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
  # i4 command in list menu
  elif int1 == 'i4':
      print("\n")
      msg = """
      Chlorine is a chemical element with the symbol Cl and atomic number 17. It belongs to the halogen group in the periodic table and is a yellow-green gas with a strong, pungent odor. It is used for water disinfection, the production of plastics like PVC, and various chemical industries.
      """
      cc = Console()
      cc.print(msg, style="bold")
      print("\n")
  elif int1 == "i5": #i5 task
      print("chlorina\n coming soon...")
  elif int1 == "i6": #i6 task
      pass
  elif int1 == "i7":
      print("exit...")
      break
  else:
      c1 = Console()
      c1.print(f"error, please right a word from the list.",style="bold red")
