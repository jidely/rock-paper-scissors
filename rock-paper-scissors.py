import random

# User and Computer Score
user_score = 0
computer_score = 0

#Total Game

total_game = 5
played_game = 0

#  Define Possible moves
options = ["rock", "paper", "scissors"]
#            0        1          2
round_number = 1

while True:
    # Input for game
    user_input = input('Type Rock/Paper/Scissors or Q to exit: ').lower()
    print(f'Round {round_number}')
    if user_input == 'q':
        break
    # Wrong input
    if user_input not in options:
        print('Type something valid')
        continue
    
    random_number = random.randint(0,2)
    #rock :0 , paper:1, scissors: 2
    computer_pick = options[random_number]
    print(f'Computer: {computer_pick}. ')
    round_number += 1
    # Check the winner add score
    if user_input == 'rock'and computer_pick == 'scissors':
        print('you win the round!')
        user_score += 1
        
    elif user_input == 'paper'and computer_pick == 'rock':
        print('you wind the round')
        user_score += 1
        
    elif user_input == 'scissors'and computer_pick == 'paper':
        print('you wind the round')
        user_score += 1
    
    elif user_input == computer_pick:
        print("It's a tie ")

    else:
        print('you lost the round')
        computer_score += 1

    # Number of games
    played_game += 1
    if played_game == total_game:
        if user_score > computer_score:
            print(f'You won, your score is {user_score}/{total_game}')
            break
        elif computer_score > user_score:
            print(f'Computer won, your score is {user_score}/{total_game}')
            break
        elif computer_score == user_score:
            print(f"It's a tie, computers score is {computer_score}, your score is {user_score}")
            break
    
    if user_score == 3:
        print(f'You won, your score is {user_score}/{total_game}')
        break
    elif computer_score == 3:
        print(f'Computer won, your score is {user_score}/{total_game}')
        break




print('Good Bye!')

