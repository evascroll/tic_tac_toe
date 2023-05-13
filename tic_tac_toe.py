# board layout
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def display_board():
    print(str(board[0]) + " | " + str(board[1]) + " | " + str(board[2]))
    print("---------")
    print(str(board[3]) + " | " + str(board[4]) + " | " + str(board[5]))
    print("---------")
    print(str(board[6]) + " | " + str(board[7]) + " | " + str(board[8]))

# input from player
def get_move(board, player):
    while True:
        move = input("Player " + player + ", enter a number between 1-9: ")
        if move.isdigit() and int(move) in board:
            return int(move)
        else:
            print("Invalid move. Please try again.")

# update board
def update_board(board, move, symbol):
    board[board.index(move)] = symbol

