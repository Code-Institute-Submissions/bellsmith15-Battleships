def get_sales_data(self):
    # while True:
        # self.clear_display()
        print((" ") * 16 + f"These sea charts belong to Captain")
        print((" ") * 4 + "Map of your Fleet:              "
                "         Guess tracker:")
        print("    0  1  2  3  4  5  6  7  8  9             "
                "0  1  2  3  4  5  6  7  8  9")
        print("  +--+--+--+--+--+--+--+--+--+--           "
                "+--+--+--+--+--+--+--+--+--+--")
        for index, row in enumerate(zip(self.board, self.guess_board)):
            print(
                    # Number rows on placement board
                f'{str(index) + " |":3s}',
                    # print row by row with 3 spaces between
                ''.join(f'{str(x):3s}' for x in row[0]),
                    # separate the two boards by 5 spaces
                ' ' * 5,
                    # Number rows on guess board
                f'{str(index)+" |" :3s}',
                    # print row by row with 3 spaces between
                ''.join(f'{str(x):3s}' for x in row[1]),
            )
        print("\n")

# def main():
#     """
#     Run all program functions
#     """
#     data = get_sales_data()

# print("Welcome to Love Sandwiches Data Automation")
# print((" ") * 16 + f"These sea charts belong to Captain")
# print((" ") * 4 + "Map of your Fleet:              "
#                 "         Guess tracker:")
# print("    0  1  2  3  4  5  6  7  8  9             "
#                 "0  1  2  3  4  5  6  7  8  9")
# print("  +--+--+--+--+--+--+--+--+--+--           "
#                 "+--+--+--+--+--+--+--+--+--+--")
# main()


print((" ") * 16 + f"These sea charts belong to Captain")
print((" ") * 4 + "Player 1 grid:              "
      "         Computer grid:")
print("    0  1  2  3  4  5  6  7  8  9             "
      "0  1  2  3  4  5  6  7  8  9")
print("  +--+--+--+--+--+--+--+--+--+--           "
      "+--+--+--+--+--+--+--+--+--+--")
for index, row in enumerate(zip()):
    print(
                # Number rows on placement board
        f'{str(index) + " |":3s}',
                # print row by row with 3 spaces between
        ''.join(f'{str(x):3s}' for x in row[0]),
                # separate the two boards by 5 spaces
        ' ' * 5,
                # Number rows on guess board
        f'{str(index)+" |" :3s}',
                # print row by row with 3 spaces between
        ''.join(f'{str(x):3s}' for x in row[1]),
        )
print("\n")



from random import randint

board = []

for x in range(0,5):
    board.append(['0'] * 5)

def print_board(board):
    for row in board:
        print(' '.join(row))

print("Lets play Battleships")
print_board(board)

def random_row(board):
    return randint(0,len(board)-1)

def random_col(board):
    return randint(0,len(board[0])-1)

ship_row = random_row(board)
ship_col = random_col(board)
print(ship_row)
print(ship_col)


for turn in range(4):
    print("Turn", turn + 1)

    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))
    # print(ship_row)
    # print(ship_col)

    if guess_row == ship_row and guess_col == ship_col:
        print("HIT! You sank their battleship")
        print("Game Over")
        break

    else:
        if (guess_row < 0 or guess_row > 4) or \
        (guess_col < 0 or guess_col > 4):
            print("Oops out of grid area")
        elif(board[guess_row][guess_col] == "X"):
            print("You guessed that spot already")
        else:
            print("You missed my battleship")
            board[guess_row][guess_col]="X"
            if turn != 4:
                print("Game Over")
            print_board(board)



    # if [guess_row not in range(5)] or \
    # [guess_col not in range(5)]:
    #      print("Oops out of grid")
    # else:


    # else:
    #     print ("You missed my battleship")
    #     board[guess_row][guess_col] = "x"
    #     print_board(board)


# working
#     if guess_row == ship_row and guess_col == ship_col:
#     print("Congrats You sank their battleship")
# else:
#     if (guess_row not in range(5)) or \
#     (guess_col not in range(5)):
#          print("Oops out of grid")
#     else:
#         print("You missed my battleship")
#         board[guess_row][guess_col]="X"
#         print_board(board)