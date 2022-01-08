# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# https://pypi.org/project/getch/
from getch import pause


# https://www.w3schools.com/python/gloss_python_class_init.asp

class Object:
    def __init__(self, start_coordinate, direction, coordinates):
        self.start_coordinate = start_coordinate
        self.direction = direction
        self.damaged_tiles = []
        self.coordinates = coordinates
        self.is_sunk = False

# Carrier, which has five holes.
# Battleship, which has four holes.
# Cruiser, which has three holes.
# Submarine, which has three holes.
# Destroyer, which has two holes.

# https://www.w3schools.com/python/python_classes.asp

class Carrier(Object):
name = "Carrier"
length = 5
symbol_list = ["C"] * length

class Carrier(Object):
name = "Battleship"
length = 4
symbol_list = ["B"] * length

class Carrier(Object):
name = "Cruiser"
length = 3
symbol_list = ["R"] * length

class Carrier(Object):
name = "Submarine"
length = 3
symbol_list = ["S"] * length

class Carrier(Object):
name = "Destroyer"
length = 2
symbol_list = ["D"] * length