def startGame():
  rock = '''
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
  '''
  
  paper = '''
      _______
  ---'   ____)____
            ______)
            _______)
           _______)
  ---.__________)
  '''
  
  scissors = '''
      _______
  ---'   ____)____
            ______)
         __________)
        (____)
  ---.__(___)
  '''
  
  #Write your code below this line 👇
  #Always import random
  import random
  #Turn variables into list
  rockpaperscissors = ["rock","paper","scissors"]
  #User Choice
  userplayer = input("\nrock, paper, or scissors?\n").lower()
  print("\n")
  playerchoice = rockpaperscissors.index(userplayer)
  if playerchoice == 0:
    print("You: \n "+ rock)
  elif playerchoice == 1:
    print("You: \n "+ paper)
  elif playerchoice ==2:
    print("You: \n "+ scissors)
  else:
    print("Error.")
  
  #Computer
  computerplayer = random.randint(0,2)
  if computerplayer == 0:
    print("Computer: \n "+ rock)
  elif computerplayer == 1:
    print("Computer: \n "+ paper)
  elif computerplayer ==2:
    print("Computer: \n "+ scissors)
  else:
    print("Error.")
  
  if playerchoice == computerplayer:
    print("It's a draw!")
  elif playerchoice == 0 and computerplayer == 1:
    print("You lose! :(")
  elif playerchoice == 0 and computerplayer == 2:
    print ("You win! :D")
  elif playerchoice == 1 and computerplayer == 0:
    print("You win! :D")
  elif playerchoice == 1 and computerplayer == 2:
    print("You lose! :(")
  elif playerchoice == 2 and computerplayer == 0:
    print("You lose! :(")
  elif playerchoice == 2 and computerplayer == 1:
    print("You win! :D")

playAgain = "yes"
while playAgain.lower() == "yes":
    startGame()
    playAgain = input("\nDo you want to start again? (yes/no)\n")
print("Thanks for playing!")