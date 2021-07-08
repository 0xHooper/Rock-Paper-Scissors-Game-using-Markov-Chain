import random as rand
import numpy as np


def check_play(player_move, response):
    if player_move == response:
        return 0
    elif player_move == 'r' and response == 'p' or \
            player_move == 'p' and response == 's' or \
            player_move == 's' and response == 'r':
        return -1
    else:
        return 1


history = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
possible_moves = ['r', 'p', 's', 'q']
possible_response = ['r', 'p', 's']
wins, losses, draws = 0, 0, 0
previous_move = -1
response = ''


def get_response():
    # if the player move wasn't used before, program will just response with rock
    if previous_move not in [0, 1, 2] or sum(history[previous_move]) == 0:
        return 'r'
    predicted_move = np.random.choice(possible_response, p=[history[previous_move][0]/sum(history[previous_move]),
                                                            history[previous_move][1]/sum(history[previous_move]),
                                                            history[previous_move][2]/sum(history[previous_move])])
    if predicted_move == 'r':
        return 'p'
    elif predicted_move == 'p':
        return 's'
    else:
        return 'r'


def tour():
    global wins, draws, losses, previous_move

    play_result = check_play(move, response)
    if play_result == 1:
        wins += 1
    elif play_result == 0:
        draws += 1
    else:
        losses += 1
    print('You played rock, program played', response)
    print('Wins', wins, 'Losses', losses, 'Draws', draws)
    if previous_move in [0, 1, 2]:
        history[previous_move][player_move] += 1
    previous_move = player_move


if __name__ == '__main__':
    while True:
        move = input('Type r,p,s, or q\n')

        while move not in possible_moves:
            move = input('Try again!\nType r,p,s, or q\n')

        response = get_response()
        if move == 'q':
            quit()
        elif move == 'r':
            player_move = 0
        elif move == 'p':
            player_move = 1
        elif move == 's':
            player_move = 2
        tour()
