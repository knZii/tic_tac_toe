import math
# current state of the game
game = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

# return current state of the game in the human readble format (STRING)
def print_game(game):
    out = ""
    for i in game:
        out += f"{i[0]}|{i[1]}|{i[2]}\n"
        out += "-----\n"
    return out

# change game 2D matrix with given input (no logic just change)
def change_game(game, position, played):
    i = math.ceil(position/3)-1
    j = (position+2)%3
    game[i][j]=played
    return game

