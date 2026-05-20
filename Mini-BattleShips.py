import random

# Mini Battleship Terminal Game
# Portfolio Project for Codecademy

# This project will use:
# - a hidden board
# - a visible board
# - random ship placement
# - player guesses
# - hit/miss logic
# - a win/loss game loop

#function creates a 5 x 5 board in a list
#creates/stores an empty list
#loops 5 times and append 'O' to list with 5 arrays being added
#returns board in a single line list
def Create_Board():
    board = []

    for row in range(5):
        board.append(['O']*5)
    
    return board

