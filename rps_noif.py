import random

random.seed(42)

while True:
	print("Make your guess:", end=" ")
	guess = str(input())
	guess = guess.lower()
	print("you guessed", guess)
	choices = ['rock', 'paper', 'scissors']
	computer_guess = random.choice(choices)
	print("computer guessed", computer_guess)
	guess_dict = {'rock': 0, 'paper': 1, 'scissors': 2}
	guess_idx = guess_dict.get(guess, 3)
	computer_idx = guess_dict.get(computer_guess)
	result_matrix = [[0,2,1],
					 [1,0,2],
					 [2,1,0],
					 [3,3,3]]
	result_idx = result_matrix[guess_idx][computer_idx]
	result_messages = ["it is a tie", "You win!!! Congrats", 'the computer wins :(', 'invalid guess']
	result = result_messages[result_idx]
	print(result)
	print()