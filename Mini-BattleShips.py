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
# - 'x' = HIT
# - 'O' = Water
# - 'S' = Ship
# - '-' = Miss

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

#function replaces characters in Hidden_Board list with 'S' to indicate ship is on that coordinate
#ship variable stores the count of ships placed on board
#loops until 3 ships have been placed on board
#Row variable stores a random integer between the ranges of 1-5
#Column variable stores a random integer between the ranges of 1-5
#If hidden board at index row,column equals water('O') then,
#the string at that index will change to 'S' to indicate a ship was placed at that coordinate
#also increases the increment of ships placed on the board by 1
#returns the updated hidden board with ships placed
def Place_Ship(Hidden_Board):
    ships = 0
    while ships < 3:
        Row = random.randint(0,4)
        Column = random.randint(0,4)

        if Hidden_Board[Row][Column] == 'O':
            Hidden_Board[Row][Column] = 'S'
            ships += 1

    return Hidden_Board

#function will ask user for numbers between 1-5 for Rows and Columns and wont stop the function until valid numbers are given
#Guess variable stored False inidicating invalid numbers from the beginning of the function
#while loops set to false and will loop continously until valid numbers are given
#Row variable will store an integer input ranging from 1-5
#Column variable will store and integer input ranging from 1-5
#if statement checks if number for row is in range of 1-5
#elif statement checks if number for Column is in range of 1-5
#else statement converts Guess to True
#Subtracts 1 from row and column since the 5x5 boards are stored in a list starting from 0-4
#returns valid Row and Columns numbers
def Ask_Guess():
    Guess = False

    while Guess == False:
        Row = int(input('Guess a number between 1-5 for row: ',))
        Column = int(input('Guess a number between 1-5 for Column: '))

        if Row < 1 or Row > 5:
            print('Row Number not between 1-5 try again.')
        elif Column < 1 or Column > 5:
            print('Column Number not between 1-5 try again')
        else:
            Guess = True

    Row -= 1
    Column -= 1

    return Row, Column

#function returns a string based on the coordinates the user has guessed;
#uses 4 parameters Hidden_Board and Visible_Board used to compare with user guessed inputs for row and column,
#if statement checks if visible board at guessed input of row and column from user has already been used
#prints a string and returns 'Duplicate'
def Update_Board(Hidden_Board, Visible_Board, Guess_Row, Guess_Column):
    if Visible_Board[Guess_Row][Guess_Column] == 'X' or Visible_Board[Guess_Row][Guess_Column] == '-':
        print('You already guessed this location')
        return 'duplicate'
    elif Hidden_Board[Guess_Row][Guess_Column] == 'S':
        Visible_Board[Guess_Row][Guess_Column] = 'X'
        print('Hit!')
        return 'hit'
    else:
        Visible_Board[Guess_Row][Guess_Column] = '-'
        print('Miss')
        return 'Miss'


#runs all other functions together to make script that plays out Battleship
#function creates 2 boards: Hidden, Visible Boards
#function places ship on hidden board that is only seen to the dev not the player
#creates and stores values of ships left on the board and how many guesses the player has left
#loops until either ships remaining or guesses remaining equals 0
#function displays visible board to show starting of the game
#prints 2 statements that show ships and guess remaining to the user
#creates and stores random numbers 1-5 into variables row and columns
#another variable storing result from another function that gets the result of the user guess
#if else statement that checks the result and updates ships and guesses remaining accordingly
#function displays board to user again after their guess has been updated both boards accordingly
#if else statement that prints out the win/loss statement depending on if the user made the guesses correctly or not
def Play_Game():
    Hidden_Board = Create_Board()
    Visible_Board = Create_Board()
    
    Place_Ship(Hidden_Board)

    Ships_Remaining = 3
    Guess_Remaining = 10

    while Ships_Remaining > 0 and Guess_Remaining > 0:
        display_board(Visible_Board)

        print('Ships Remaining:', Ships_Remaining)
        print('Guess Remaining:', Guess_Remaining)

        Row, Column = Ask_Guess()

        Result = Update_Board(Hidden_Board, Visible_Board, Row, Column)

        if Result == 'hit':
            Ships_Remaining -= 1
            Guess_Remaining -= 1
        elif Result == 'Miss':
            Guess_Remaining -= 1
        elif Result == 'duplicate':
            print('Duplicate guess you did not loose your turn.')

        display_board(Visible_Board)

    if Ships_Remaining == 0:
        print('You found all the ships. YOU WIN!')
    else:
        print('You ran out of guesses. YOU LOSE!')


Player1 = Play_Game()