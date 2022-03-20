from random import randint

playerWins = 0
computerWins = 0
win = 5
rock = 'rock'
paper = 'paper'
scissor = 'scissor'


while computerWins < win and playerWins < win:
    print(f'Player: {playerWins}, Computer: {computerWins}')
    print("...rock...")
    print("...paper...")
    print("...scissor...")

    player = input("Enter your choice: ")
    random_num = randint(0, 2)
    if random_num == 0:
        computer = "rock"
    elif random_num == 1:
        computer = "paper"
    else:
        computer = "scissor"

    print(f"The computer picks: {computer}")

    if player == computer:
        print("It's a TIE!")
    elif player == 'quit':
        break
    elif player == 'rock':
        if computer == 'paper':
            print('Computer WIN!')
            print(f'Computer')
            computerWins += 1
        elif computer == 'scissor':
            print('Player WIN!')
            playerWins += 1
    elif player == 'scissor':
        if computer == 'rock':
            print('Computer WIN!')
            computerWins += 1
        elif computer == 'paper':
            print('Player WIN!')
            playerWins += 1
    elif player == 'paper':
        if computer == 'scissor':
            print('Computer WIN!')
            computerWins += 1
        elif computer == 'rock':
            print('Player WIN!')
            playerWins += 1
    else:
        print('Please enter the correct value')

print('FINAL SCORE...')
print(f'Player: {playerWins}, Computer: {computerWins}')

if playerWins > computerWins:
    print('Congrats, you win!')
elif playerWins < computerWins:
    print('You lose!')
else:
    print('Thank you for playing')
