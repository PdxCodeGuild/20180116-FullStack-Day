#requirements
# 7 columns, 6 rows
# 2 players, red & black, take turns adding chips
# win - 4 chips in a row, diagonal/ vertical/ horizontal

# design & planning
# board - list of lists of ints
	# string containing names of colors
# player
	# players manually entering col number
	# dumb ai makes random choices
	# v2- smart ai using min/ max
# user interface
	#draw board
		# add pipes or underscores for board so it doesnt look empty
	#prompt user for column they want to drop chip in
	#play again?
# program architecture
	# win/ lose function
# game mechanics
	# win condition- 4 horizontal, vertical, or diagonal
	# adding too may pieces for column

import random


def print_board(board, piece_lookup):
	for j in range(len(board)):
		for i in range(len(board[j])):
			print(piece_lookup[board[j][i]], end='')
		print()


def put_piece(board, column, piece):
	row = 0
	while row < len(board) and board[row][column] == 0:
		row += 1
	row -= 1
	board[row][column] = piece


# BOARD GEN
n_columns = 7
n_rows = 6
piece_lookup = [' ', 'O ', 'X ']
board = [[0 for j in range(n_columns)] for i in range(n_rows)]
# ALTERNATIVE FOR BOARD GEN^
# board = []
# for i in range(n_rows):
# 	board.append([])
# 	for j in range(n_columns):
# 		board[i].append(0)

# RANDOM TESTING
# for i in range(20):
# 	piece = random.randint(1, 2)
# 	column = random.randint(0, len(board[0]) - 1)
# 	put_piece(board, column, piece)

print('welcome to our collect 4 game!\n')
print('-' * 80)

players = [1, 2]
current_player_id = random.randint(0, len(players) - 1)

while True:
	print_board(board, piece_lookup)

	while True:
		column = input(f'player {current_player_id}, choose a column (1 - {n_columns}: ')
		try:
			column = int(column)
			column -= 1
			if 0 <= column < n_columns:
				break
		except ValueError:
			print('please enter a number')

	piece = current_player_id + 1
	put_piece(board, column, piece)

	current_player_id += 1
	current_player_id %= len(players)


print_board(board, piece_lookup)
