# from random import randint

# board = []

# for x in range(0,5):
#     board.append(['0'] * 5)

# def print_board(board):
#     for row in board:
#         print(' '.join(row))

# print("Lets play Battleships")
# print_board(board)

# def random_row(board):
#     return randint(0,len(board)-1)

# def random_col(board):
#     return randint(0,len(board[0])-1)


# ship_row = random_row(board)
# ship_col = random_col(board)
# # print(ship_row)
# # print(ship_col)


# for turn in range(4):
#     print("Turn", turn + 1)

#     guess_row = int(input("Guess Row: "))
#     guess_col = int(input("Guess Col: "))
#     # print(ship_row)
#     # print(ship_col)

#     if guess_row == ship_row and guess_col == ship_col:
#         print("HIT! You sank their battleship")
#         print("Game Over")
#         break

#     else:
#         if (guess_row < 0 or guess_row > 4) or \
#         (guess_col < 0 or guess_col > 4):
#             print("Oops out of grid area")
#         elif(board[guess_row][guess_col] == "X"):
#             print("You guessed that spot already")
#         else:
#             print("You missed my battleship")
#             board[guess_row][guess_col]="X"
#             if turn != 4:
#                 print("Game Over")
#             print_board(board)

# --------------------------------------------------------------------------------

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
    """ Prints the board """
    return randint(0, len(board)-1)


def random_col():
    """ Prints the board """
    return randint(0, len(board[0])-1)


ship_row = random_row()
ship_col = random_col()


for turn in range(6):
    print("Turn", turn + 1)

    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))
    # Guess the row of where the ship is on the board
    if guess_row == ship_row and guess_col == ship_col:
        print("HIT! You sank their battleship")
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
                # print_board()
        # print("Game Over")

#             if turn != 4:
#                 print("Game Over")
#             print_board(board)































































































# from random import randint

# board = []

# for x in range(0, 10):
#     board.append(['.'] * 10)


# def print_board():
#     """ Prints the board """
#     for row in board:
#         print(' '.join(row))


# print("Lets play Battleships")
# print_board()


# def random_row():
#     """ Prints the board """
#     return randint(0, len(board)-1)


# def random_col():
#     """ Prints the board """
#     return randint(0, len(board[0])-1)


# ship_row = random_row()
# ship_col = random_col()
# # print(ship_row)
# # print(ship_col)


# for turn in range(4):
#     print("Turn", turn + 1)

#     guess_row = int(input("Guess Row: "))
#     guess_col = int(input("Guess Col: "))
#     # Guess the row of where the ship is on the board
#     if guess_row == ship_row and guess_col == ship_col:
#         print("HIT! You sank their battleship")
#         print("Game Over")
#         break

#     else:
#         if guess_row < 0 or guess_row > 10 or guess_col < 0 or guess_col > 10:
#             print("Oops out of grid area")
#         elif(board[guess_row][guess_col] == "X"):
#             print("You guessed that spot already")
#         else:
#             print("You missed my battleship")
#             board[guess_row][guess_col] = "X"
#             if turn != 4:
#                 print_board()
            #     print("Game Over")
            # print_board()
