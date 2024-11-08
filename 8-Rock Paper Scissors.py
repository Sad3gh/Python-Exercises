def play_rps(player1, player2):
    options = ['rock','paper','scissors']
    #validating inputs
    if player1 not in options or player2 not in options:
        return "invalid input. Please choose 'rock', 'paper' or 'scissors'."

    #determining the winner
    if player1 == player2:
        return "It's a tie!"
    elif (player1 == 'rock' and player2 == 'scissors') or \
         (player1 == 'paper' and player2 == 'rock') or \
         (player1 == 'scissors' and player2 == 'paper'):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

#test cases
print(play_rps('paper','rock'))
print(play_rps("rock","scissors"))