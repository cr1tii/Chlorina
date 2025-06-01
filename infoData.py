from rich.console import Console

# first we set a list of the elements types

def ret():
    lis = ["non-metal","noble gas","alkali metal","alkali metal earth","metaloid","halogen","post-transtion metal","transtion metal","lanthanide","to exit"]
    for index, item in enumerate(lis,start=1):
        print(index, item)

# close the def and start a new one for non-metal
# non-metal informations

def non_metal(): 
    console = Console()
    console.print("\n1. NON-METAL",style="bold underline color(94)")
    msg = """
    These are some of the most essential elements for life. Non-metals are generally poor conductors of heat and electricity. Many are gases at room temperature (like oxygen and nitrogen), while others are brittle solids (like sulfur). Unlike metals, they tend to gain electrons in chemical reactions, forming negative ions.\n\nThey play a central role in biology, medicine, and industry. For example, oxygen sustains life, carbon forms the backbone of organic molecules, and nitrogen is a critical component of DNA and fertilizers.
    """
    console.print(msg,style="bold")
    print("\n\n")
    list1 = [" Hydrogen (H)"," Oxygen (O)"," Nitrogen (N)"," Carbon (C)"," Sulfur (S)"]
    console.print("Examples :",style="bold underline")
    for t in list1:
       console.print(t, style="color(94)")

    
    msg2 = """
       Discovery:\n
Hydrogen: Identified by Henry Cavendish in 1766.\n
Oxygen: Discovered independently by Carl Wilhelm Scheele (1772) and Joseph Priestley (1774).\n
Nitrogen: Isolated by Daniel Rutherford in 1772.\n
Carbon: Known since ancient times in forms like charcoal and diamond.\n
Sulfur: Recognized since antiquity; used in ancient alchemy.\n\n
Significance: Non-metals are essential for life and various chemical processes.
       """
    console.print(msg2, style="bold")


#2 open another def but for noble gasses information

def noble():
    console = Console()
    console.print("2. NOBLE GAS\n\n",style="underline bold color(8)")
    msg3 = """
    These are some of the most reactive elements in the periodic table. Lithium, sodium, and potassium fall into this group. They are soft, silvery metals that react violently with water, releasing hydrogen gas and forming strong bases (alkalis). Despite their reactivity, they’re incredibly useful: lithium powers our modern batteries, sodium is essential for nerve function, and potassium is a crucial nutrient in plants and humans alike.
    """
    console.print(msg3, style="bold ")
    print("\n\n")
    list2 = [" Helium (He)"," Neon (Ne)"," Argon (Ar)"," Krypton (Kr)"," Xenon (Xe)"," Radon (Rn)"]
    console.print("Examples: ",style="bold underline")
    for L in list2:
        console.print(L,style = "color(94)")
        
    msg4 = """
    Discovery:\n
Helium: First observed in the solar spectrum by Pierre Janssen and Joseph Norman Lockyer in 1868; isolated on Earth by William Ramsay in 1895.\n
Argon: Discovered by Lord Rayleigh and William Ramsay in 1894.\n
Neon, Krypton, Xenon: Isolated by William Ramsay and Morris Travers in 1898.\n
Radon: Identified by Friedrich Ernst Dorn in 1900.\n\n
Significance: These inert gases have applications in lighting, welding, and as inert environments for chemical reactions.
    """
    console.print(msg4, style="bold")

#we start alkali metals

def alk_metals():
    console = Console()
    console.print("3. ALKALI METALS",style="bold color(12) underline")
    print("\n")
    msg5 = """
    These are some of the most reactive elements in the periodic table. Lithium, sodium, and potassium fall into this group. They are soft, silvery metals that react violently with water, releasing hydrogen gas and forming strong bases (alkalis). Despite their reactivity, they’re incredibly useful: lithium powers our modern batteries, sodium is essential for nerve function, and potassium is a crucial nutrient in plants and humans alike.
    """
    console.print(msg5,style="bold")
    print("\n\n")
    console.print("Exmaples: ",style="bold underline")
    list3 = [" Lithium (Li)"," Sodium (Na)"," Potassium (K)"," Rubidium (Rb)"," Cesium (Cs)"," Francium (Fr)"]
    for bruh in list3:
        console.print(bruh,style="color(8)")

    msg6 = """
    Discovery:\n
Lithium: Discovered by Johan August Arfvedson in 1817.\n
Sodium & Potassium: Isolated by Humphry Davy in 1807 through electrolysis.\n
Rubidium & Cesium: Identified by Robert Bunsen and Gustav Kirchhoff using spectroscopy in 1860-1861.\n
Francium: Discovered by Marguerite Perey in 1939.\n\n
Significance: Highly reactive metals used in batteries, glass production, and as heat exchange mediums.
    """
    console.print(msg6,style="bold")

# we start alkaline earth metals

def alk_earth():
    console = Console()
    console.print("4. ALKALINE EARTH METALS",style="bold underline color(31)")
    print("\n")

    msg7 = """
    Less reactive than their alkali neighbors, the alkaline earth metals include magnesium and calcium. These metals are harder and have higher melting points. Calcium is indispensable for strong bones and teeth, while magnesium is used in lightweight alloys and even fireworks. They form oxides and hydroxides that are basic in nature — hence the name “alkaline.”
    """
    console.print(msg7,style="bold")
    print("\n\n")
    console.print("Examples: ","bold underline color(8)")
    list4 = [" Beryllium (Be)"," Magnesium (Mg)"," Calcium (Ca)"," Strontium (Sr)"," Barium (Ba)"," Radium (Ra)"]
    for l4 in list4:
        console.print(l4,style="color(94)")

    msg8 = """
    Discovery:\n
Beryllium: Identified by Louis-Nicolas Vauquelin in 1798.\n
Magnesium: Recognized as an element by Joseph Black in 1755.\n
Calcium: Isolated by Humphry Davy in 1808.\n
Strontium: Discovered by Adair Crawford in 1790.\n
Barium: Isolated by Humphry Davy in 1808.\n
Radium: Discovered by Marie and Pierre Curie in 1898.
    """
    console.print(msg8, style="bold")

#we start another def but for metalloids

def metalloids():
    console = Console()
    console.print("5. METALLOIDS",style="bold underline color(31)")
    print("\n")

    msg9 = """
    Metalloids sit on the fence — literally — between metals and non-metals on the periodic table. Elements like boron, silicon, and arsenic exhibit a fascinating mix of both metallic and non-metallic traits. Silicon, for example, is the backbone of the tech industry, used in semiconductors and microchips. Metalloids are vital for innovations in electronics, solar panels, and chemical sensors.
    """
    console.print(msg9,style="bold")
    print("\n\n")
    console.print("Examples: ",style="bold underline ")
    list5 = [" Boron (B)"," Silicon (Si)"," Arsenic (As)"," Antimony (Sb)"," Tellurium (Te)"]
    for l5 in list5:
        console.print(l5,style="color(94)")

    msg10 = """
    Discovery:

Boron: Isolated by Humphry Davy in 1808.\n
Silicon: Identified by Jöns Jacob Berzelius in 1824.\n
Arsenic: Known since ancient times; recognized as an element in the Middle Ages.\n
Antimony: Known since ancient times; isolated in the 15th century.\n
Tellurium: Discovered by Franz-Joseph Müller von Reichenstein in 1782.\n\n
Significance: Metalloids have properties intermediate between metals and non-metals, making them useful in semiconductors and alloys.
    """
    console.print(msg10,style="bold ")

#we close the def and start another one for halogens

def halogens():
    con = Console()
    con.print("6. HALOGENS",style="bold underline pink1")
    print("\n")
    msg11 = """
    The halogens — such as fluorine, chlorine, bromine, and iodine — are highly reactive non-metals. They readily form salts when combined with metals (hence the name “halogen,” meaning “salt-former” in Greek). Chlorine is widely used in disinfection and water treatment, fluorine is added to toothpaste to prevent cavities, and iodine is crucial for thyroid health. Their reactivity decreases down the group, but their usefulness remains high.
    """
    con.print(msg11,style="bold")
    print("\n\n")

    con.print("Examples: ",style="bold underline")
    list6 = [" Fluorine (F)"," Chlorine (Cl)"," Bromine (Br)"," Iodine (I)"," Astatine (At)"]
    for l6 in list6:
        con.print(l6,style="color(94)")

    msg12 = """
    Discovery:\n
Fluorine: Isolated by Henri Moissan in 1886.\n
Chlorine: Discovered by Carl Wilhelm Scheele in 1774.\n
Bromine: Identified by Antoine Jérôme Balard in 1826.\n
Iodine: Discovered by Bernard Courtois in 1811.\n
Astatine: Synthesized by Dale R. Corson, Kenneth Ross MacKenzie, and Emilio Segrè in 1940.\n\n
Significance: Halogens are highly reactive and are used in disinfectants, pharmaceuticals, and halogen lamps.
    """
    con.print(msg12,style="bold")

# we close this and again start another def

def post_metals():
    con = Console()
    con.print("7. POST-TRANSTION METALS",style="bold underline color(177)")
    print("\n")
    msg13 = """
    These are metals with characteristics somewhat similar to the transition metals, but generally softer, with lower melting points. Aluminum, tin, and lead are common examples. Aluminum is lightweight and corrosion-resistant, used in aircraft, cans, and foil. Tin is used in coatings to prevent rust, and lead, despite its toxicity, has been used in batteries and radiation shields.
    """
    con.print(msg13,style="bold")
    print("\n\n")
    
    con.print("Examples: ",style="bold underline")
    list7 = [" Aluminum (Al)"," Gallium (Ga)"," Indium (In)"," Tin (Sn)"," Thallium (Tl)"," Lead (Pb)"," Bismuth (Bi)"]
    for l7 in list7:
        con.print(l7,style="color(94)")

    msg14 = """
    Discovery:\n
Aluminum: Isolated by Hans Christian Ørsted in 1825.\n
Gallium: Discovered by Paul-Émile Lecoq de Boisbaudran in 1875.\n
Indium: Identified by Ferdinand Reich and Hieronymous Theodor Richter in 1863.\n
Tin: Known since ancient times; used in bronze alloys.\n
Thallium: Discovered by William Crookes in 1861.\n
Lead: Known since ancient times; used in pipes and paints.\n
Bismuth: Known since ancient times; often confused with lead and tin.\n\n
Significance: These metals are softer and have lower melting points, making them useful in solders, batteries, and shielding materials.
    """
    con.print(msg14,style="bold")

#we close this and start anothet def

def trans_metals():
    con = Console()
    con.print("8. TRANSITION METALS",style="bold underline color(53)")
    print("\n")

    msg15 = """
    Perhaps the most well-known and widely used metals, the transition metals include iron, copper, zinc, and silver. They are strong, durable, and often form colorful compounds. These elements are responsible for construction materials, electrical wiring, coinage, and even biological processes (like iron in hemoglobin). Their ability to exist in multiple oxidation states makes them crucial for catalysis and chemical reactions.
    """
    con.print(msg15,style="bold")
    print("\n\n")

    con.print("Examples: ",style="bold underline")
    list8 = [" Iron (Fe)"," Copper (Cu)"," Nickel (Ni)"," Zinc (Zn)"," Silver (Ag)"," Gold (Au)"," Platinum (Pt)"]
    for l8 in list8:
        con.print(l8,style="color(94)")

    msg16 = """
    Discovery:\n
Iron, Copper, Silver, Gold: Known since prehistoric times; used in tools, currency, and jewelry.\n
Nickel: Identified by Axel Fredrik Cronstedt in 1751.\n
Zinc: Recognized as a distinct element in the 16th century\n
Platinum: Known to South American cultures before European discovery in the 16th century.\n\n
Significance: Transition me
    """
    con.print(msg16,style="bold")

#we close this and start the last def

def lanth():
    con = Console()
    con.print("9. LANTHANIDES",style="bold underline color(60)")
    print("\n")
    msg17 = """
    The lanthanides are a series of rare earth metals with unique magnetic and optical properties. Neodymium is used in powerful magnets, europium in red and blue phosphors for screens, and cerium in catalytic converters. Though not as rare as their name suggests, they are difficult to extract and purify. These elements are key to modern technology — from smartphones to hybrid vehicles to renewable energy systems.
    """
    con.print(msg17,style="bold")
    print("\n\n")
    con.print("Examples: ")
    list8 = [" Lanthanum (La)"," Cerium (Ce)"," Neodymium (Nd)"," Europium (Eu)"," Gadolinium (Gd)"]
    for l8 in list8:
        con.print(l8,style="color(94)")

    msg18 = """
    Discovery:\n
Lanthanum: Discovered by Carl Gustaf Mosander in 1839.\n
Cerium: Identified independently by Jöns Jakob Berzelius and Wilhelm Hisinger, and by Martin Heinrich Klaproth in 1803.\n
Neodymium: Separated from didymium by Carl Auer von Welsbach in 1885.\n
Europium: Discovered by Eugène-Anatole Demarçay in 1896.\n
Gadolinium: Identified by Jean Charles Galissard de Marignac in 1880.\n\n
Significance: Lanthanides are known for their magnetic and luminescent properties, making them valuable in electronics, lasers, and as catalysts.
    """
    con.print(msg18,style="bold")

def main():
    while True:
        ret()
        con = Console()
        con.print("type a mumber: ",end=" ",style="color(94)")
        inp11 = input()
        if inp11 ==str(1):
            non_metal()
        elif inp11 == str(2):
            noble()
        elif inp11 == str(3):
            alk_metals()
        elif inp11 == str(4):
            alk_earth()
        elif inp11 == str(5):
            metalloids()
        elif inp11 == str(6):
            halogens()
        elif inp11 == str(7):
            post_metals()
        elif inp11 == str(8):
            trans_metals()
        elif inp11 == str(9):
            lanth()
        elif inp11 == str(10):
            break

if __name__ == "__main__":
    main()
