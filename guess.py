from random import randint
number = randint(1,10)
guess = None    #in while loop variable has to be declared first
 
while True:
	guess = input("Guess a number between 1 - 10: ")
	while guess == "":
		guess = input("Enter a value: ")
	guess = int(guess)
	if guess < number:
		print("too low")	
	elif guess > number:
		print("too high")
	else:
		print("You won")
		again = input("do you want to keep playing? (y/n) ")
		while again != "y" and again != "n":
			again = input("Enter valid value (y/n): ")
		if again == "y":      # place "if"  outside while loop # **
			number = randint(1,10)
			guess = None
		else:
			break
				