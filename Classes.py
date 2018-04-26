from random import randint
from time import sleep

class Coin:
  
  def __init__(self, name):
    self.name = name
    self.sideUp = 'Heads'
    
  def flip(self):
    if randint(0, 1) == 0:
      self.sideUp = 'Heads'
    else:
      self.sideUp = 'Tails'
  
  def displayInfo(self):
    self.flip()
    print("{} flipped {}".format(self.name, self.getSide()))
  
  def getSide(self):
    return self.sideUp
    
    
class Die:
  
  def __init__(self, numSides):
    self.numSides = numSides
    self.sideUp = 1
    
  def roll(self):
    self.sideUp = randint(1, self.numSides)
    
  def displayInfo(self):
    self.roll()
    print("D{} rolled a {}".format(self.numSides, self.getSide()))
  
  def getSide(self):
    return self.sideUp
    
dime = Coin('Dime')
penny = Coin('Penny')
quarter = Coin('Quarter')
nickel = Coin('Nickel')

d6 = Die(6)
d20 = Die(20)

for x in range(100):
  dime.displayInfo()
  penny.displayInfo()
  quarter.displayInfo()
  nickel.displayInfo()
  d6.displayInfo()
  d20.displayInfo()
  print('\n')
  
  
  if dime.sideUp == 'Heads' and penny.sideUp == 'Heads' and quarter.sideUp == 'Heads' and nickel.sideUp == 'Heads':
    print("All heads!")
    
  elif dime.sideUp == 'Tails' and penny.sideUp == 'Tails' and quarter.sideUp == 'Tails' and nickel.sideUp == 'Tails':
    print("All tails!")
    
  elif d6.sideUp == 6 and d20.sideUp == 20:
    print("Max numbers on both dice!")
    
  elif d6.sideUp == 1 and d20.sideUp == 1:
    print("Minimum numbers on both dice!")
    
  elif d6.sideUp == d20.sideUp:
    print("Both dice are equal!")
    
  elif dime.sideUp == 'Heads' and penny.sideUp == 'Heads' and quarter.sideUp == 'Heads' and nickel.sideUp == 'Heads' and d6.sideUp == 6 and d20.sideUp == 20:
    print("All heads and max numbers on dice!")
    
  elif dime.sideUp == 'Tails' and penny.sideUp == 'Tails' and quarter.sideUp == 'Tails' and nickel.sideUp == 'Tails' and d6.sideUp == 1 and d20.sideUp == 1:
    print("All tails and minimum numbers on dice!")
    
  print('\n')
  sleep(2)
