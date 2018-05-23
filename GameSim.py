#Austin Beard

import random
import sys
import time

#Damage func
def Dmg():
    Dmg = random.randint(1,6)
    return Dmg

#Healing func
def Restore():
    Restore = random.randint(1,4)
    return Restore
    
#Players name
CharName = input("Name your character: ")

#Opponents name
OppName = input("Name your opponent: ")

#Starting values

CharHp = 50
OppHp = 50
turn = 1
potion = 1

Ready = input("Are you ready to begin?(y/n): ").lower()

#Catch statement for input
if (Ready == "n"):
    sys.exit(0)

elif (Ready != 'y'):
    print("Invalid input\nPlease try again")
    sys.exit(0)

#Delay between attacks
Delay = input("Would you like delay after each attack?(y/n): ").lower()

if (Delay != 'y' and Delay != 'n'):
        print("Invalid input\nPlease try again")
        sys.exit(0)
        
#Main loop
while (CharHp > 0 or OppHp > 0):
    print("\n\nTURN",turn)
    
    #Restoration
    if (turn % 4 == 0):
        
        #Player potion
        Healing = Restore()
        print("\nPOTION #",potion)
        print(CharName,"restored", Healing, "health")
        CharHp = CharHp + Healing
        
        if (Delay == 'y'):
            time.sleep(1)
            
        potion = potion + 1
        
    #Player's Attack
    print("\n"+ CharName +"'s turn")
    Damage = Dmg()
    print(CharName, "attacked", OppName, "for", Damage)
    OppHp = OppHp - Damage
    print(OppName, "has", OppHp, "health")
    
    #Opponent dies player wins
    if (OppHp <= 0):
        print(CharName,"won with",CharHp,"health")
        print(OppName,"lost")
        break
        
    if (Delay == 'y'):
        time.sleep(2)
    
    #Opponent's Attack
    print("\n"+ OppName +"'s turn")
    OppDamage = Dmg()
    print(OppName, "attacked", CharName, "for", OppDamage)
    CharHp = CharHp - OppDamage
    print(CharName,"has", CharHp, "health")
    
    #Player dies opponent wins
    if (CharHp <= 0):
        print(OppName,"won with", OppHp,"health")
        print(CharName,"lost")
        break
        
    if (Delay == 'y'):
        time.sleep(2)
    
    turn += 1
    
#Hold screen if python file is ran not in command prompt
print("\n\nPress any key to continue...")