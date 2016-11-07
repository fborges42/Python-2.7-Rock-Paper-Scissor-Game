import random

optionList = ["Rock","Paper","Scissors"]
playAgain = "yes"

def RockPaperScissors():
	humanChoice = input("1- Rock, 2- Paper, 3- Scissors\n")
	if humanChoice == 1:
		humanChoice = "Rock"
	elif humanChoice == 2:
		humanChoice = "Paper"
	else:
		humanChoice = "Scissors"
	
	computerChoice = random.choice(optionList)
	
	if humanChoice == computerChoice:
		print "It's a draw!"

	if humanChoice == "Rock":
		if computerChoice == "Paper": 
			print "Computer Wins!"
		if computerChoice == "Scissors": 
			print "You Win!"
	elif humanChoice == "Paper": 
		if computerChoice == "Rock": 
			print "You Win!"
		if computerChoice == "Scissors": 
			print "Computer Wins!"
	else: 
		if computerChoice == "Rock": 
			print "Computer Wins!"
		if computerChoice == "Paper": 
			print "You Win!"

	print "Your choice was " + str(humanChoice)
	print "Computer choice was " + str(computerChoice)

while playAgain.lower() == "yes":
	RockPaperScissors()
	print('Do you want to play again? (yes or no)')
	playAgain = raw_input().lower()
