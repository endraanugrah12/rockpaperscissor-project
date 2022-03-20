print('...rock...')
print('...paper...')
print('...scissor...')

player1 = input('player1, Enter your choice: ')

print('\n **NO CHEATING** \n' * 20)

player2 = input('player2, Enter your choice: ')



if player1 == 'rock' and player2 == 'paper':
    print('player2 WON!')
elif player1 == 'scissor' and player2 == 'paper':
    print('player1 WON!')
elif player1 == 'scissor' and player2 == 'rock':
    print('player2 WON!')
elif player2 == 'rock' and player1 == 'paper':
    print('player1 WON!')
elif player2 == 'scissor' and player1 == 'paper':
    print('player2 WON!')
elif player2 == 'scissor' and player1 == 'rock':
    print('player1 WON!')
elif player1 == player2:
    print('TIE')
else:
    print('You entered the wrong value')
