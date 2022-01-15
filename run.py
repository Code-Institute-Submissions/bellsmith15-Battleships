from random import randint

board = []

for x in range(0, 10):
    board.append(['.'] * 10)


def print_board():
    """ Prints the board """
    for row in board:
        print(' '.join(row))


print("Lets play Battleships")
print_board()


def random_row():
    """ Computer randomly picks the row of the ship """
    return randint(0, len(board)-1)


def random_col():
    """ Computer randomly picks the column of the ship """
    return randint(0, len(board[0])-1)


ship_row = random_row()
ship_col = random_col()


for turn in range(6):
    print("Turn", turn + 1)

    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))
    # Guess the row and column of where the ship is on the board
    if guess_row == ship_row and guess_col == ship_col:
        print("HIT! You sank the battleship")
        print("Game Over")
        break

    else:
        if guess_row < 0 or guess_row > 9 or guess_col < 0 or guess_col > 9:
            print("Oops out of grid area")
        elif(board[guess_row][guess_col] == "X"):
            print("You guessed that spot already")
        else:
            print("You missed my battleship")
            board[guess_row][guess_col] = "X"
            if turn == 5:
                print("Game Over")
        print_board()
