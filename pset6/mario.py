# Usage
# $ python mario.py
# Height: 3
#   #
#  ##
# ###

from cs50 import get_int

# prompt the user for height input
height = get_int("Height: ")
while height <= 0 or height >= 9:
    height = get_int("Height: ")

line = 1
for x in range(height):
    for y in range(height - line):
        print(" ", end = "")
    for z in range (line):
        print("#", end = "")
    print()
    line += 1