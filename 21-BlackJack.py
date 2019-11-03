#21 BlackJack
#Author: Ayesha Khalid
#Description: User vs computer in a game of 21 BlackJack

#assign your variables 
totalPoints=0
userLoss=0
userWins=0
userTie=0
compTie=0
compLoss = 0
compWins= 0

import random
import time

#defining suits for random suit generator 
def suits ():
    suit=random.randint(1,4)
    if suit == 1:
        return "♦"
    elif suit == 2:
        return "♥"
    elif suit == 3:
        return "♣"
    else:
        return "♠"
suitType=suits()         
#defining cards 
def drawCard ():
   card=random.randint(2,14)
   if card<=10:
      return card
   elif card==11:
      return'J'
   elif card==12:
      return 'Q'
   elif card==13:
      return 'K'
   else:
      return 'A'
#defining points
def points (card):
   if card == "J" or card =="Q" or card =="K":
      return 10
   elif card == "A":
      if totalPoints >= 11:
         return 1
      if totalPoints == 10:
         return 11
      if totalPoints < 10:
         userIn= input("\n You have drawn an Ace. Do you want the ace to be a 1 or a 11? ")
         if userIn == "1":
     #if user selects 1 then 1 would be added to total points
            return 1
         elif userIn == "11":
     #if user selects 11 then 11 would be added to total points
            return 11
   elif card <= 10:
      return card

computerPoints=0
#defining computer points
def comPoints (card1):
   if card1 == "J" or card1 =="Q" or card1 =="K":
      return 10
   elif card1 == "A":
      if computerPoints >= 11:
         return 1
      elif computerPoints <= 10:
         return 11
   elif card1 <= 10:
      return card1
    
#defining fuction to output user's cards
def  outputCard(a):
    return ("\n+ ------------- +" + "\n|\t\t|" + "\n|\t" + str(card)+ str(suitType)+ "\t|" + "\n|\t\t|" + "\n+ ------------- +")

#defining fuction to output computer's cards
def  outputCard1(a):
    return ("\n+ ------------- +" + "\n|\t\t|" + "\n|\t" + str(card1)+ str(suitType)+ "\t|" + "\n|\t\t|" + "\n+ ------------- +")


#welcoming the user to the game
print("\t\tWelcome to 21 BlackJack!\t\t")
print('\t******ENJOY!!!May the best hand win.******\t')
hands=int(input("\nHow many hands do you want to play: "))
games=hands

#loops "hand" amout of times for user
for hands in range (0,hands):
   cards=2
   print('\nYour hand will begin in 3 seconds get ready to play!!!')
   time.sleep(3)
   totalPoints= 0
   computerPoints=0
   print('\n\n******NEW HAND!!!******')
   for counter in range (0,2):
      card = drawCard()
      totalPoints = totalPoints + points(card)
      print(outputCard(card))
      print ("\n Your total points are now " + str(totalPoints))
      time.sleep(1.5)

#while the user points is less than 21, it will ask user to hit or stand      
   while totalPoints<21:
      user=input('\n Press s for Stand or h for Hit: ')
      if user=='H' or user == 'h':
            card = drawCard()
            totalPoints = totalPoints + points(card)
            suitType=suits()
            print(outputCard(card))
            print ("\n Your total points are now " + str(totalPoints))
            cards=cards+1
            if cards==5 and totalPoints<21:
                  print('\n Since you have reached 5 cards you have won this hand. Congratulations!!!')
                  userWins=userWins+1
                  break
            if totalPoints>21:
                  break
      elif user=="s" or user=="S":
                  break

#checking if user wins or losses
   if totalPoints>21:
       print('\n You Bust! Sorry you lost this hand. Therefore, the computer wins this hand.')
       userLoss= userLoss+1
       compWins= compWins+1
   elif totalPoints==21:
       print('\n Congratulations you won this hand. Therefore, the computer loses this hand. ')
       userWins =userWins + 1
       compLoss=compLoss+1

#if user chooses to stand, then the computer will be dealt the cards and play it's hand
   else:
       print("\n Now the computer will be dealt cards")
       time.sleep(2)

       #loop for the 2 starting hand cards
       for counter in range (0,2):
           card1 = drawCard()
           computerPoints = computerPoints + comPoints(card1)
           suitType=suits()
           print(outputCard1(card1))
           print ("\n The computer's total points are now " + str(computerPoints))
           time.sleep(1.5)
           
       #while computer points is less than user's total points it will keep outputting cards    
       while computerPoints<totalPoints:
             card1 = drawCard()
             computerPoints = computerPoints + comPoints(card1)
             suitType=suits()
             print(outputCard1(card1))
             print ("\n The computer's total points are now " + str(computerPoints))
             time.sleep(2)

       #checking wins, loses or ties and adjusting the scoreboard accordingly      
       if computerPoints>totalPoints and computerPoints<21:
             compWins=compWins+1
             userLoss=userLoss+1
             print('\n The computer wins this hand!!!')
       elif computerPoints>21:
             print('\n The computer bust therefore user wins this hand!!!')
             userWins= userWins+1
             compLoss= compLoss+1
       elif computerPoints==totalPoints:
            print('\n You and the computer have tied')
            userTie=userTie+1
            compTie=compTie+1
       elif computerPoints==21:
           ('The computer has 21 points, therefore the computer wins')
           compWins=compWins+1
           userLoss=userLoss+1
                     
    #outputting the scoreboard        
   time.sleep(1.5)         
   print ('\n '+"*" * 55)
   print(" User wins: "+str(userWins)+ "|" + " User ties: "+str(userTie)+"|" + " User losses: "+ str(userLoss))
   print(' '+"*" * 55)
   print(" Computer wins: "+str(compWins)+ "|" + " Computer ties: "+str(compTie)+"|" +" Computer losses: " + str(compLoss))
   print(" " + "*" * 55)

   #asking user if they want to quit the next hands
   time.sleep(2)
   games=games-1
   if games!=0:
       userQuit=input('\n Do you want to quit, Yes or No:')
       if userQuit=='yes' or userQuit=="Yes" or userQuit=='y' or userQuit=="Y":
            print("\n Hope you had fun playing BlackJack, can't wait to see you again!!!")
            #if user quits they break out of the loop, resulting in ending the loop
            break
   elif games==0:
       print("\n You have played all your hands. Hope you had fun playing BlackJack, can't wait to see you again!!!")
            
