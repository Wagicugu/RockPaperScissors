#name: Joan  Waweru
#Section: 2.1
#Date: 4th May, 2018

player1 = input('Player 1?')
player2 = input('Player 2?')

if player1 == 'rock' and player2 == 'paper':
         print ('Player 2 wins!')
         
    elif player1 == 'rock' and player2 == 'scissors': 
         print ('Player 2 wins!')
    elif player1 == 'rock' and player2 == 'rock':
         print ('Its a tie!')
    elif player1 == 'paper' and player2 == 'rock':
         print ('Player 1 wins!)
    elif player1 == 'paper' and player2 == 'scissors':
         print ('Player 2 wins!)
    elif player1  == 'paper' and player2 == 'paper':
         print ('Its a tie')
    elif player1 == 'scissors' and player2 == 'rock':
         print ('Player 1 wins!)
    elif player1 == 'scissors' and player2 == 'paper':
         print ('Player 1 wins!)
    elif player1 == 'scissors' and player2 == 'scissors':
         print ('Its a tie!)
    else:
         print ('Invalid input') 
