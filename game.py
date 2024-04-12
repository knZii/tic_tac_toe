import math


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

# check if the current game (given matrix) has winner then return the winner 
def check_winner(game):
    # check possible row wins
    for i in game:
        if i[0] == i[1] == i[2]:
            return i[0]
    # check possible column win
    for i in range(3):
        if game[0][i] == game[1][i] == game[2][i]:
            return game[0][i]
    # check possible diagonal win
    if game[0][0] == game[1][1] == game[2][2]:
        return game[0][0]
    if game [0][2] == game [1][1] == game [2][0]:
        return game [0][2]
    return None

def two_player_game():
    # current state of the game
    game = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]]
    turn = False # False = X  | True = O
    for _ in range(9):
        if check_winner(game) != None:
            break
        print(print_game(game))
        inp = input(f"Select number you want to play ({"O" if turn else "X"}): ")
        inp = int(inp)
        game = change_game(game, inp, "O" if turn else "X")
        turn = not turn
    if check_winner(game) == None:
        print("Tie game!")
    else:
        print(f"{check_winner(game)} win the game Nice!")
two_player_game()