import os
from readchar import readkey, key

x = 0
y = 1

my_possition = [3, 1]
map_width = 30
map_height = 15

while True:
    print("+" + "-" * (map_width*2) + "+")

    for cordenate_y in range(map_height):
        print("|", end="")
        for cordenate_x in range(map_width):
            if my_possition[x] == cordenate_x and my_possition[y] == cordenate_y:
                print(":)", end="")
            else:
                print("  ", end="")
        print("|")

    print("+" + "-" * (map_width*2) + "+")

    direction = readkey()

    if direction == "w":
        my_possition[y] -= 1
        my_possition[y] %= map_height
    elif direction == "s":
        my_possition[y] += 1
        my_possition[y] %= map_height
    elif direction == "a":
        my_possition[x] -= 1
        my_possition[x] %= map_width
    elif direction == "d":
        my_possition[x] += 1
        my_possition[x] %= map_width
    elif direction == "q":
        break

    os.system("cls")
