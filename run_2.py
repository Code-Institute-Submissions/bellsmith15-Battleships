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