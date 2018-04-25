from random import choice, randint
from time import sleep

class Coin:
  sides = ['heads', 'tails']
  
  def __init__(self, name):
    self.name = name
    
  def flip(self):
    side = choice(Coin.sides)
    return side
  
  def displayInfo(self):
    print("{} flipped {}".format(self.name, self.flip()))
    
    
class Die:
  
  def __init__(self, numSides):
    self.numSides = numSides
    
  def roll(self):
    side = randint(1, self.numSides)
    return side
    
  def displayInfo(self):
    print("D{} rolled a {}".format(self.numSides, self.roll()))
    
dime = Coin('Dime')
penny = Coin('Penny')
quarter = Coin('Quarter')
nickel = Coin('Nickel')

d6 = Die(6)
d20 = Die(20)

for x in range(10):
  dime.displayInfo()
  penny.displayInfo()
  quarter.displayInfo()
  nickel.displayInfo()
  d6.displayInfo()
  d20.displayInfo()
  print("\n")
  sleep(2)
