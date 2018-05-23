#Austin Beard

import random

#Bomb damage
def dmg():
    bombDmg = random.randint(1,4)
    return bombDmg

#User
baseBombs = 20
run = 0

#Enemy base hp
targA = 25
targB = 25

#Main
while(targA > 0 or targB > 0):
    run += 1
    carrying = 2
    print("\n\nBomb run", run)
    
    #Attack on first base
    if (targA > 0):
        bomb1 = dmg()
        print("\nBomb did", bomb1, "damage to base A.")
        for i in range(bomb1):
            targA -= 1
            print("Base A has", targA)
        carrying -= 1
        
        #Drop 2 bombs on first base if second is destroyed
        if (targB <= 0 and targA > 0):
            bomb2x = dmg()
            print("\nSecond bomb did", bomb2x, "damage to base A.")
            for i in range(bomb2x):
                targA -= 1
                print("Base A has",targA)
            
    #Attack on second base        
    if (targB > 0):
        bomb2 = dmg()
        print("\nBomb did", bomb2, "damage to base B.")
        for i in range(bomb2):
            targB -= 1
            print("Base B has",targB)
        carrying -= 1
        
        #Drop 2 bombs on second base if first is destroyed
        if (targA <= 0 and targB > 0 and carrying == 1):
            bomb2x = dmg()
            print("\nSecond bomb did", bomb2x, "damage to base B.")
            for i in range(bomb2x):
                targB -= 1
                print("Base B has",targB)
    
    #Get out of loop
    if (baseBombs == 0 or (targA <= 0 and targB <= 0)):
        break
    
    #Resupply bombs
    elif (baseBombs > 0):
        print("\nResupplying bombs")
        for i in range(2):
            baseBombs -= 1
            print("We have", baseBombs, "left at base")
    
print("\nTarget A has", targA, " health, target B has", targB, "health and there are", baseBombs, "bombs remaining.")

#Outcome statement
if (targA <= 0 and targB <= 0):
    print("We got them! Let's head home")
    
elif (run == 11):
    print("We ran out of bombs!")