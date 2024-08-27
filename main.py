import random

user_wins = 0
computer_wins = 0

choices = ['rock', 'paper', 'scissors']
while True:
    user_input = input("Type Rock/Paper/Scissors or press Q to quit: ").lower()
    if user_input == 'q':
        break

    if user_input not in choices:
        continue

    random_number = random.randint(0, 2)
    computer_choice = choices[random_number]
    print('Computer chooses', computer_choice)

    if user_input == 'rock' and computer_choice == 'scissors':
        print('You Win!')
        user_wins += 1

    elif user_input == 'paper' and computer_choice == 'rock':
        print('You Win!')
        user_wins += 1

    elif user_input == 'scissors' and computer_choice == 'paper':
        print('You Win!')
        user_wins += 1

    elif user_input == computer_choice:
        print('Draw!')

    else:
        print('You lose!')
        computer_wins += 1

print('You won', user_wins, 'times.')
print('The computer won', computer_wins, 'times.')
print("Thanks for playing!")