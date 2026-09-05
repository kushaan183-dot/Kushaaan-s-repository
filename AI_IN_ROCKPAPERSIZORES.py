import random
from colorama import init, Fore, Style
init(autoreset=True)


def player_choise():
	choice = ''
	while choice not in ['rock', 'paper', 'scissors']:
		choice = input(
			Fore.GREEN + "Choose rock, paper, or scissors: " + Style.RESET_ALL
		).strip().lower()
		if choice not in ['rock', 'paper', 'scissors']:
			print("Invalid choice, try again.")
	return choice


def ai_move(player_choice):
	while True:
		ai_choice = random.choice(['rock', 'paper', 'scissors'])
		if ai_choice != player_choice:
			return ai_choice


def check_win(player_choice, ai_choice):
	if player_choice == ai_choice:
		return 'tie'
	elif (player_choice == 'rock' and ai_choice == 'scissors') or (player_choice == 'paper' and ai_choice == 'rock') or (player_choice == 'scissors' and ai_choice == 'paper'):
		return 'player'
	else:
		return 'ai'


def rock_paper_scissors():
	print("Welcome to Rock, Paper, Scissors!")
	player_name = input(Fore.GREEN + "Enter your name: " + Style.RESET_ALL)
	if not player_name:
		player_name = "Player"

	while True:
		print(Fore.GREEN + "Your turn" + Style.RESET_ALL)
		player_choice_value = player_choise()
		print(Fore.RED + "AI's turn" + Style.RESET_ALL)
		ai_choice_value = ai_move(player_choice_value)

		print(f"{player_name} chose: {player_choice_value}")
		print(f"AI chose: {ai_choice_value}")

		result = check_win(player_choice_value, ai_choice_value)
		if result == 'player':
			print(Fore.GREEN + f"Congratulations {player_name}! You won!" + Style.RESET_ALL)
		elif result == 'ai':
			print(Fore.RED + "AI won! Better luck next time!" + Style.RESET_ALL)
		else:
			print(Fore.YELLOW + "It's a tie!" + Style.RESET_ALL)

		again = input(Fore.CYAN + "Play again? (yes or no) " + Style.RESET_ALL).strip().lower()
		if again == 'yes':
			print(Fore.CYAN + "Starting a new game..." + Style.RESET_ALL)
			continue
		print(Fore.CYAN + "Thanks for playing!" + Style.RESET_ALL)
		break


if __name__ == "__main__":
	rock_paper_scissors()
