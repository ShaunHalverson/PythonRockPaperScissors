import random

print("Welcome to Rock Paper Scissors!")
print("-------------------------------")

### Set up variables
cpuScore = 0
playerScore = 0
tieScore = 0
possibleHands = ["Rock","Paper","Scissors"]

def checkForWinner(playerHand, computerHand):
  if(playerHand == "Rock" and computerHand == "Paper"):
    print("Sorry you lost :(")
    return "Cpu"
  elif(playerHand == "Rock" and computerHand == "Scissors"):
    print("Congrats! You have won :)")
    return "Player"
  elif(playerHand == "Scissors" and computerHand == "Paper"):
    print("Congrats! You win :)")
    return "Player"
  elif(playerHand == "Scissors" and computerHand == "Rock"):
    print("Sorry, you lost!")
    return "Cpu"
  elif(playerHand == "Paper" and computerHand == "Rock"):
    print("Congrats! You win :)")
    return "Player"
  elif(playerHand == "Paper" and computerHand == "Scissors"):
    print("Sorry, you lost!")
    return "Cpu"
  else:
    print("It's a tie, play again!")
    return "Tie"

### Start game loop
while(playerScore != 3 and cpuScore != 3):
  ### Validate input
  while True:
    playerHand = input("\nPick a hand. Rock, Paper, or Scissors: ")
    if(playerHand == "Rock" or playerHand == "Paper" or playerHand == "Scissors"):
      break
    else:
      print("Invalid input. Try again.")
  
  ### Generate computer pick
  computerHand = random.choice(possibleHands)

  ### Print results
  print("Your hand: ", playerHand)
  print("Cpu hand: ", computerHand)
  result = checkForWinner(playerHand, computerHand)
  if(result == "Player"):
    playerScore += 1
  elif(result == "Cpu"):
    cpuScore += 1
  else:
    tieScore += 1
  print("Your score: ", playerScore, "CPU: ", cpuScore, "Ties: ", tieScore)

print("Game over! Thank you for playing :)")
