import random2
import math
class Item:
  def __init__(self,level):
    self.isSuper = False
    self.isSupr = False
    self.isInv = False
    self.strength=0;
    self.life=0;
    self.chanceOfGettingHit=0;
    self.chanceOfHitting=100;
    self.turns=0
    self.generateName()
    self.generateStats(level)

  def generateName(self):
    f=open("ItemList.txt")
    names = f.read().splitlines()
    self.maxindex=len(names)
    self.index=random2.randint(0,len(names)-1)
    self.name = names[self.index]
  def generateStats(self,level):
    enhancment = random2.randint(0,6)
    chance = random2.randint(0,100)
    if self.name == "Potion of Strength":
      self.strength = random2.randint(2,6+enhancment+math.ceil(level/2))
      if chance<15:
        self.isSuper = True
        self.name += " and Life"
        self.life = random2.randint(2,6+enhancment+math.ceil(level/2))
      self.turns = random2.randint(2,6)
    elif self.name == "Potion of Life":
      self.life = random2.randint(6,12+enhancment+level)
      if chance>75:
        self.isSuper = True
        self.name += " and Strength"
        self.strength = random2.randint(1,3+enhancment+math.ceil(level/2))
      if not self.isSuper:
        self.turns=1
    elif self.name == "Potion of Invincibility":
      self.isInv = True
      self.chanceOfGettingHit=100
      self.turns = random2.randint(2,6)
    elif self.name == "Potion of Superiority":
      self.isSupr = True
      self.chanceOfHitting=100
      self.turns = random2.randint(2,6)



