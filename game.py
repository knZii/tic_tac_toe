# current state of the game
game = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# return current state of the game in the human readble format (STRING)
def print_game(game):
    out = ""
    for i in game:
        out += f"{i[0]}|{i[1]}|{i[2]}\n"
        out += "-----\n"
    return out

print(print_game(game))