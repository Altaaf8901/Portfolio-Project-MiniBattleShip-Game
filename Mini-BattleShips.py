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

#function outputs list into a 5 x 5 board
#Row_num stores the count for what row is being printed
#prints the columns numbered accordingly to the 5 x 5 board
#loops through each row in board;
#print is converting Row_number to a string and then puts spaces in between each word
#Row_num is being added by 1 to increase count of which row from the list of boards is being printed
def display_board(Visible_Board):
    Row_Num = 1

    print(' ', 1, 2, 3, 4, 5)
    for row in Visible_Board:
        print(str(Row_Num) + ' ' + ' '.join(row))
        Row_Num += 1





Visible_Board = Create_Board()
Hidden_Board = Create_Board()
display_board(Visible_Board)