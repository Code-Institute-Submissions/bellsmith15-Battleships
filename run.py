from random import randint

computer_board = []
player_board = []
NUM_SHIPS = 7


def how_play():

    """
    This function starts the game and introduces the
    player to instructions on how to play the game
    """
    print((" ") * 16 + "   Let's Play Battleships!")
    print("\n")
    print("How to Play the Game:")
    print("The aim is to sink your opponents ship.")
    print("Each row uses co-ordinates of (0,9) across 8 rows.")
    print("Inputs must use numbers between (0,6) for row and column, eg.(0,0)")
    print("Board is represented by a grid of dots")
    print("Hits are marked with a * and Misses are markeds by x")
    print("You have 10 go's to sink the ship.")


for x in range(0, 7):
    computer_board.append(['.'] * 7)
    player_board.append(['.'] * 7)
    # This for loop creates a list of 8 rows it then
    # appends this array with dots to represent board


def player_board_app(p_board):
    """
    Prints to the player board
    """
    for rows in p_board:
        print(' '.join(rows))


def computer_board_app(c_board):
    """
    Prints to the computers board
    """
    for row in c_board:
        print(' '.join(row))


def rand_col(c_board):
    """
    This function picks a random column for
    the ship on the computer board
    """
    return randint(0, len(c_board[0]) - 1)


def rand_row(c_board):
    """
    This function picks a random row for
    the ship on the computer board
    """
    return round(randint(0, len(c_board) - 1))


def battleship():
    """
    This function of the game holds all the loops that are carried out
    """
    how_play()
    comp_row = rand_row(computer_board)
    comp_col = rand_col(computer_board)
    player_destroyed = 0
    computer_destroyed = 0
    player_name = input("Enter name: \n")

    set_ships = set()
    # this varible calculates the number of
    # ships that have been placed on the board
    p_ship = 0
    while len(set_ships) < NUM_SHIPS:
        player_row = input("Place ship by row: \n")
        player_col = input("Place ship by column: \n")

        # this checks if the data entered for the rows
        # and columns is a digit and then
        # lets the player know if its incorrect
        # or if it the data has already been entered
        if player_col.isdigit() and player_row.isdigit():
            player_col = int(player_col)
            player_row = int(player_row)

            if player_row < 0 or player_row > 6 or \
                    player_col < 0 or player_col > 6:
                print("Oops out of grid area")
                print("Choose again between 0 and 6")
            elif(player_row, player_col) in set_ships:
                print("A ship sails here already")
            else:
                set_ships.add((player_row, player_col))
                player_board[player_row][player_col] = "S"
                # if true, then increase the number printed
                p_ship = p_ship + 1
                print("Great - ship's placed: ", p_ship)
        else:
            # if false print error message
            print("A digit has not been entered correctly \n"
                  f"You have only placed, ({p_ship}) ships")
    for turn in range(10):
        print("Turn", turn + 1)
        player_guess_row = int(input("Guess Row across) to target: \n"))
        player_guess_col = int(input("Guess Col (down) to target: \n"))
        print("\n")
        print(f"Coordinates ({player_guess_row},{player_guess_col}) Fire!")

        comp_guess_row = round(randint(0, len(player_board)-1))
        comp_guess_col = round(randint(0, len(player_board)-1))

        # Guess logic for the player row and column
        # of where the ship is on the board
        if player_guess_row < int(0) or player_guess_row > int(6) or \
                (player_guess_col < 0 or player_guess_col > 6):
            print("Not even near it")
        elif player_board[player_guess_row][player_guess_col] == "*":
            print("Already Sunk this one!")
        elif (player_guess_row == comp_row and
                player_guess_col == comp_col):
            print("Battlship SUNK!")
            player_board[player_guess_row][player_guess_col] = "*"
            computer_board[player_guess_row][player_guess_col] = "*"
            computer_destroyed += 1
        else:
            if (player_guess_row < 0 or player_guess_row < 6) or\
                    (player_guess_col < 0 or player_guess_col < 6):
                print("Not even near")
            elif player_board[player_guess_row][player_guess_col] == "x":
                print("Already Sunk this one!")
            else:
                print("You missed this time")

        # Guess logic for the computer row and column
        # of where the ship is on the board
        print(f"Computer aims ({comp_guess_row},{comp_guess_col}) Fire!")
        if comp_guess_row == player_row and comp_guess_col == player_col:
            player_board[comp_guess_row][comp_guess_col] = "*"
            computer_board[comp_guess_row][comp_guess_col] = "*"
            print("Computer HIT and SINKS!")
            player_destroyed += 1
        else:
            player_board[comp_guess_row][comp_guess_col] = "x"
            computer_board[comp_guess_row][comp_guess_col] = "x"
            print("They missed you this time")

        print("\n")
        print("Guess Computer board")
        computer_board_app(computer_board)
        print(f"\n{player_name}\'s board")
        player_board_app(player_board)
        print("\n")

        if turn == 9:
            print("GAME OVER ...play again")
            break
        else:
            print("...play again")
        if computer_destroyed == 1:
            print("Computer ships are all hit")
            break

        if player_destroyed == 1:
            print("The Computer has won")
            print("GAME OVER!")
            break


player_board_app(player_board)
computer_board_app(computer_board)
rand_col(computer_board)
rand_row(computer_board)

battleship()
