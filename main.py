import os 
import logging

from random import choice

POSSIBILITIES = {
    0 : ('rock','scissors'),
    1 : ('paper','rock'),
    2 : ('scissors','paper')
}

scoreboard = {
    -1: ['Machine', 0],
    0: ['Ties', 0],
    1: ['Player', 0]
}

def clear():
    os.system('clear')

def throw_message_plus_lines(message):
    line = '=' * len(message)
    print(line, message, line, sep='\n')

def welcome():
    throw_message_plus_lines('Welcome to Rock Paper Scissors Game')

def throw_message(*messages):
    for message in messages:
        print(message)

def choose():
    throw_message(
        'Choose:',
        ' | '.join([f'{item[0]} - {item[1][0].upper()}' for item in POSSIBILITIES.items()])
    )
    text = input()
    number = int(text) if text in ''.join([str(key) for key in POSSIBILITIES.keys()]) else 0
    return number

def find_winner(player_move, machine_move):
    if machine_move == player_move:
        return 0
    if POSSIBILITIES[machine_move][1] == POSSIBILITIES[player_move][0]:
        return -1
    elif POSSIBILITIES[player_move][1] == POSSIBILITIES[machine_move][0]:
        return 1
    
    return None

def show_move(player_move, machine_move, winner):
    scoreboard[winner][1] += 1
    winner_name = scoreboard[winner][0]
    winning_message = f'{winner_name} won!' if 'Tie' not in winner_name else 'Tie!!'
    throw_message(
        '='*10,
        f'Player move: {POSSIBILITIES[player_move][0].upper()}',
        f'Machine move: {POSSIBILITIES[machine_move][0].upper()}',
        winning_message,
        '='*10,
        '\n'
    )

def play_again():
    message = 'Play Again? 0 - YES | 1 NO'
    answer = input(message + '\n') or '0'
    clear()
    if answer == '0':
        return True
    elif answer == '1':
        return False
    else:
        play_again()

def show_scoreboard():
    throw_message(
        'SCOREBOARD:',
        '\n'.join(f'{value[0]}: {value[1]}' for value in list(scoreboard.values()))
    )

def init():
    show_scoreboard()
    player_move = choose()
    machine_move = choice(list(POSSIBILITIES.keys()))
    winner = find_winner(player_move, machine_move)
    show_move(player_move, machine_move, winner)
    if play_again():
        init()

def configure_logging():
    LOG_FORMAT = '%(levelname)s %(asctime)s - %(message)s'
    logging.basicConfig(filename="app.log", level=logging.DEBUG, format=LOG_FORMAT)
    log = logging.getLogger()
    return log

def main():
    welcome()
    log = configure_logging()
    try:
        init()
    except Exception as e:
        log.error(e)
        main()
    finally:
        throw_message_plus_lines('End of the game.')
    
main()