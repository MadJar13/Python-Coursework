import random2
from item import Item
from enemy import Enemy
import replit

class Hero:
  def __init__(self, Name):
    self.name = Name
    self.strength = 0
    self.level = 1
    self.exp=0
    self.life = 0
    self.possibleOptions=["Left","Right","Forward"]
    self.hasEncounteredEnemy=False
    self.chanceOfGettingHit=10
    self.chanceOfHitting=80
    self.isAlive=True
    self.items=[]
    f=open("WalkingList.txt")
    self.texts = f.read().splitlines()
  def gainExp (self, exp):
    self.exp += exp
    if self.exp >=1:
      self.level+=1
      print ("New Level !")
      self.exp-=1
    if self.level%3 == 0:
      self.strength += random2.randint(0,self.level)
      self.life += random2.randint(0,self.level)
      print ("You have gained extra HP and Str! Congrats!")
    if self.level%5 == 0:
      self.chanceOfGettingHit -= random2.randint(1,2)
      self.chanceOfHitting += random2.randint(1,2)
      print ("You are now more skilled!")
  def takeDamage (self, damage):
    self.life -= damage
    if self.life <=0:
      self.isAlive=False
      #die
  def itemsMadeTurn(self):
    for i in self.items:
     i.turns-=1
    self.checkItemDurability()
  def checkItemDurability (self):
    for i in self.items:
      if(i.turns<=0):
        self.strength -= i.strength
        self.chanceOfHitting -= i.chanceOfHitting
        self.chanceOfGettingHit += i.chanceOfGettingHit
        self.items.remove(i)
        del i
  def walk(self):
      self.itemsMadeTurn()
      chance=random2.randint(0,100)
      if chance<20:
        self.encounterItem(self.level)
      elif chance<40:
        self.encounterEnemy(self.level)
      else:
        text = self.texts[random2.randrange(0,len(self.texts)-1)]
        print(text)
        #read and print line from txt file for getting deeper.
      input()
      replit.clear()
  def itemEnhancments(self,item):
    self.strength += item.strength
    self.life += item.life
    self.chanceOfHitting += item.chanceOfHitting
    self.chanceOfGettingHit -= item.chanceOfGettingHit
  def encounterItem(self,lvl):
    item = Item(lvl)
    self.items.append(item)
    print("You have found ",item.name,"!")
    if item.index>=item.maxindex/2:
      print ("You will have it for the next ",item.turns," turns")
    self.itemEnhancments(item)

  def encounterEnemy(self,lvl):
    f=open("enemyEncounterings.txt")
    expressions = f.read().splitlines()
    enemy = Enemy(lvl)
    expression = expressions[random2.randint(0,len(expressions)-1)]
    print(expression,enemy.name,"!")
    if enemy.isBoss:
      print ("Oh Sh*t! He's a big one!")
    self.hasEncounteredEnemy = True
    self.Fight(enemy)
    if self.isAlive:
      print ("Well done!")
      print ("You have defeated the monster")
      print ("You have earned ",enemy.exp," experience")
      self.gainExp(enemy.exp)
      del enemy
  def Fight(self,enemy):
    print ("You have started a battle against ",enemy.name,".")
    print (enemy.name," has ",enemy.strength, " strength and ",enemy.life," health !")
    print ("Press Enter to continue !")
    input()
    replit.clear()
    while (self.isAlive == enemy.isAlive):
      print ("HP: ",self.life,"     Str:",self.strength)
      print ("\n\n\n\n\nEnemy HP: ",enemy.life,"     Enemy Str:",enemy.strength)
      if random2.randint(0,100)<self.chanceOfGettingHit:
        dmg=random2.randrange(2,enemy.strength)
        print ("AAhhh! You got hit")
        print ("You took ",dmg," damage")
        self.takeDamage(dmg)
      else:
        missmsg = ["Enemy missed","You dogged","You escaped the enemy hit", "Nice block adventurer", "Parried very well" ]
        msg = missmsg[random2.randint(0,len(missmsg)-1)]
        print (msg)
        input()
      if random2.randint(0,100)<self.chanceOfHitting:
        missmsg = ["Slash","Bam!","Knock!", "Thud...", "Might swing","Fist of Heaven","Headbanger" ]
        msg = missmsg[random2.randint(0,len(missmsg)-1)]
        print (msg)
        dmg=random2.randrange(2,self.strength)
        print ("You have dealt ",dmg, " damage to ", enemy.name, ".")
        enemy.takedamage(dmg)
      else:
        missmsg = ["Miss","Dogged","The enemy has escaped your hit", "Blocked", "Parry" ]
        msg = missmsg[random2.randint(0,len(missmsg)-1)]
        print (msg)
      input()
      replit.clear()

  def takeTurn(self):
    options = ["Left","Right","Forward"]
    self.possibleOptions=["Left","Right","Forward"]
    numberOfOptions = random2.randrange(0,10)
    if numberOfOptions < 5 :
      nopt1=5
      nopt2=5
      while (nopt1 == nopt2):
        option1 = random2.randrange(0,30)
        option2 = random2.randrange(0,30)
        if option1<10:
          nopt1=0
        elif option1<20:
          nopt1=1
        else:
          nopt1=2
        if option2<10:
          nopt2=0
        elif option2<20:
          nopt2=1
        else:
          nopt2=2
      self.possibleOptions.clear()
      self.possibleOptions.append(options[nopt1])
      self.possibleOptions.append(options[nopt2])
      
