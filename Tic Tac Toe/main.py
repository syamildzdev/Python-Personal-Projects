import os
import random


def clear():
	'''
	To clear output in cmd
	'''
	os.system('clear')

def display_board(board):
	'''
	Display game board
	'''
    clear()
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)

def player_input():
	'''
	Choose marker
	'''
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input("Player 1 : Choose your marker, X or O \n").upper()
        
    if marker == 'O':
        return ('O','X')
    elif marker == 'X':
        return ('X','O')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
	'''
	Check if a mark has won
	'''
    return ((board[1]==mark and board[2]==mark and board[3]==mark) or # Bottom 3
    (board[1]==mark and board[4]==mark and board[7]==mark) or # Left vertical
    (board[3]==mark and board[6]==mark and board[9]==mark) or # Right vertical
    (board[7]==mark and board[8]==mark and board[9]==mark) or # Top 3
    (board[1]==mark and board[5]==mark and board[9]==mark) or # Diagonal bottom left to right top
    (board[3]==mark and board[5]==mark and board[7]==mark) or # Diagonal bottom right to left top
    (board[4]==mark and board[5]==mark and board[6]==mark) or # Middle horizontal
    (board[2]==mark and board[5]==mark and board[8]==mark)) # Middle vertical

def choose_first():
	''' 
	Choose the first player
	'''
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    return (board[position]==' ')

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, position):
            return False
    return True

def player_choice(board):
    choice = int(input("Choose your next marker position \n"))
    return space_check(board, choice)

def replay():
    replay = input("Do you want to play again, y/n \n")
    if replay == 'y':
        return True
    else: 
        return False