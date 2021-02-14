from hero import Hero
import random2
import replit
import time
ans="yes"
while (ans=="yes"):
  protagonist = Hero(input("What is your name Hero? : "))
  print ("Welcome "+ protagonist.name + "!")
  time.sleep(2)
  statschoise = "no"
  while (statschoise != "yes"):
    replit.clear()
    print ("Choose your stats: ")
    startstr=random2.randrange(10,20)
    startlife=random2.randrange(10,30)
    startcogh=random2.randrange(30,80)
    startcoh=random2.randrange(30,80)
    print ("Strength: ",startstr)
    print ("Health: ",startlife)
    print ("Chance of getting hit: ",startcogh)
    print ("Chance of hitting: ",startcoh)
    print ("Do you like your stats ? (yes/no)")
    statschoise=input()
  protagonist.strength=startstr
  protagonist.life=startlife
  protagonist.chanceOfGettingHit=startcogh
  protagonist.chanceOfHitting=startcoh
  time.sleep(1)
  replit.clear()
  print ("Great! Take on your adventure. You are in a old dungeon maze full of surprises")
  time.sleep(2)
  replit.clear()
  while(protagonist.isAlive):
    print ("HP: ",protagonist.life,"     Str:",protagonist.strength,"     Lvl: ",protagonist.level,end=" ")
    print ("  Items: ",end=" ")
    for i in protagonist.items:
      print (i.name," (",i.turns," turns left), ")
    print()
    protagonist.takeTurn() 
    print("You can go ",end = " ")
    print(*protagonist.possibleOptions, sep = ", ")
    path = input("Choose your path: ")
    while (path not in protagonist.possibleOptions):
      print("Incorrect input.")
      path = input("Choose your path: ")
    protagonist.walk()
  if protagonist.isAlive:
    print ("Well done brother! You have won !!!")
  else:
    print (protagonist.name," You have died at level ",protagonist.level," and had :")
    for i in protagonist.items:
      print(i.name)
    print ("In your inventory.")
    print ("You will not be forgotten!")
    print ("\n\n\nDo you want to try again? (yes/no)")
    ans=input()
print ("Goodbye!")
time.sleep(3)