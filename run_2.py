from random import randint

NUM_SHIPS = 5

computer_board = []
player_board = []

def game_rules():

    """
    This function is triggered at the start of the game
    It prints out the rules to show players how the games works
    """
    print("Lets play Battleships")
    print("How to Play the Game:")
    print("The aim is to sink your opponents ship.")
    print("Each row uses a co-ordinates of (0,9) across 10 rows.")
    print("Inputs must use numbers between(0,7) for both the row and the column. Beginning at (0, 0).")
    print("Water is represented by . Misses are represented by X ")
    print("\n")
    print("Hits are represented by # and your ship is represented by S")
    print("You have 10 go's to sink the ship.")

# The following for loop creates an list of 8 rows
# It then populates this array with ~ which represents water


for x in range(0, 7):
    computer_board.append(['.'] * 7)
    player_board.append(['.'] * 7)


def computer_board_app(c_board):
    """
    Prints the board
    """
    for row in c_board:
        print(' '.join(row))

# computer_board_app(computer_board)

def rand_row(c_board):
    """
    This function picks a random row
    """
    return round(randint(0, len(c_board) - 1))

    rand_row(computer_board)


def rand_col(c_board):
    """
    This function picks a random column
    """
    return randint(0, len(c_board[0]) - 1)

    rand_col(computer_board)


def player_board_app(p_board):
    """
    Prints the board
    """
    for row in p_board:
        print(' '.join(row))

# player_board_app(player_board)


print((" ") * 16 + f"   Let's Play Battleships!")
print("\n")
print((" ") * 5 + "   Player grid:          "
      "          Computer grid:")
print("     0  1  2  3  4  5  6            "
      "  0  1  2  3  4  5  6            ")
print("   |==|==|==|==|==|==|==|          "
      " |==|==|==|==|==|==|==|        ")
for index, row in enumerate(zip(computer_board, player_board)):
    print(
        # Number rows on placement board
        f'{str(index) + " |":4s}',
        # print row by row with 3 spaces between
        ''.join(f'{str(x):3s}' for x in row[0]),
        # separate the two boards by 5 spaces
        ' ' * 5,
        # Number rows on guess board
        f'{str(index) + " |" :4s}',
        # print row by row with 3 spaces between
        ''.join(f'{str(x):3}' for x in row[1]),
    )
print("\n")


def main():
    """
    This function of the game holds all the loops that are carried out
    """
    game_rules()
        
    computer_row = rand_row(computer_board)
    computer_col = rand_col(computer_board)
    player_destroyed = 0
    computer_destroyed = 0
    player_name = input("Enter name: \n")

    player_ships = set()
    # this varible is number of successfull goes
    goes_number = 0
    while len(player_ships) < NUM_SHIPS:
        player_row = input("Place ship by row: \n")
        player_row = input("Place ship by column: \n")

        # this checks if the data entered for the rows and columns is a digit
        if player_col.isdigit() and player_row.isdigit():
            player_col = int(player_col)
            player_row = int(player_row)


            if player_row < 0 or player_row > 8 or player_col < 0 or player_col > 8:
            print("Oops out of grid area")
        elif(board[guess_row][guess_col] == "X"):
            print("You guessed that spot already")
        else:
            print("You missed my battleship")
            board[guess_row][guess_col] = "X"
            if turn == 5:
                print("Game Over")
        print_board()



        







# print((" ") * 16 + f"These sea charts belong to Captain")
# print((" ") * 10 + "  Player 1 grid:              "
#       "             Computer grid:")
# print("    0  1  2  3  4  5  6  7  8  9             "
#       "0  1  2  3  4  5  6  7  8  9")
# print("  +--+--+--+--+--+--+--+--+--+--           "
#       "+--+--+--+--+--+--+--+--+--+--")
# for index, row in enumerate(zip()):
#     print(
#                 # Number rows on placement board
#         f'{str(index) + " |":3s}',
#                 # print row by row with 3 spaces between
#         ''.join(f'{str(x):3s}' for x in row[0]),
#                 # separate the two boards by 5 spaces
#         ' ' * 5,
#                 # Number rows on guess board
#         f'{str(index)+" |" :3s}',
#                 # print row by row with 3 spaces between
#         ''.join(f'{str(x):3s}' for x in row[1]),
#         )
# print("\n")


# def build_board(self):
#     """
#     Builds a blank board using nested lists.
#     will be used to store the ship objects
#     """
#     self.board = []

#     for row in range(self.board_size):
#         self.board.append([])
#         for _ in range(self.board_size):
#             self.board[row].append("SHIP")
#     return self.board


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
#     """ Computer randomly picks the row of the ship """
#     return randint(0, len(board)-1)


# def random_col():
#     """ Computer randomly picks the column of the ship """
#     return randint(0, len(board[0])-1)


# ship_row = random_row()
# ship_col = random_col()


# for turn in range(6):
#     print("Turn", turn + 1)

#     guess_row = int(input("Guess Row: "))
#     guess_col = int(input("Guess Col: "))
#     # Guess the row and column of where the ship is on the board
#     if guess_row == ship_row and guess_col == ship_col:
#         print("HIT! You sank the battleship")
#         print("Game Over")
#         break

#     else:
#         if guess_row < 0 or guess_row > 9 or guess_col < 0 or guess_col > 9:
#             print("Oops out of grid area")
#         elif(board[guess_row][guess_col] == "X"):
#             print("You guessed that spot already")
#         else:
#             print("You missed my battleship")
#             board[guess_row][guess_col] = "X"
#             if turn == 5:
#                 print("Game Over")
#         print_board()

# board_size = 10

# def __init__(self, owner, auto=True):
#     self.owner = owner
#     self.auto = auto
#     self.guess_board = self.build_guess_board()
#     self.board = self.build_board()
#     self.fleet = self.build_fleet()
#     self.map_of_fleet = self.fleet_coords_map()


# def build_board(self):
#     """
#     Builds a blank board using nested lists.
#     will be used to store the shp objects
#     """
#     self.board = []

#     for row in range(self.board_size):
#         self.board.append([])
#         for _ in range(self.board_size):
#             self.board[row].append("\U000025FD")
#     return self.board

# def build_guess_board(self):
#     """"
#     Builds a blank board using nested lists
#     will be use to keep note of a players guess
#     results
#     """
#     self.guess_board = []
#     for row in range(self.board_size):
#         self.guess_board.append([])
#         for _ in range(self.board_size):
#             self.guess_board[row].append("\U000025FD")
#     return self.guess_board


# class Game():
#     """
#     Creates start of game
#     by kslsk
#     """
