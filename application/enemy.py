import random2
class Enemy:
  def __init__(self,level):
    self.life= random2.randint(20,40+10*level)
    self.strength=random2.randint(3,10+10*level)
    self.level=level
    self.isBoss=False
    self.exp=self.life*0.01-self.level*0.01
    self.isAlive=True
    self.generateName()
  def takedamage(self,damage):
    self.life-=damage
    if self.life<=0:
      self.isAlive=False
      #die
  def generateName(self):
    f=open("enemyList.txt")
    names = f.read().splitlines()
    self.name = names[random2.randint(0,len(names)-1)]
  def chanceOfBeingBoss(self):
    chance = random2.randint(0,100)
    if chance == 1 :
      self.life+=self.life-10*self.level
      self.isBoss=True

