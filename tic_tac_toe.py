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

# check for winner
def check_win(board, symbol):
    win_conditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [0, 4, 8], [2, 4, 6]]
    for condition in win_conditions:
        if all(board[i] == symbol for i in condition):
            return True
    return False

# Game loop

# Display the board to the players
    
# Prompt Player 1 for their move
  
# Check if Player 1 has won or if there is a tie
    
# Display the updated board to the players
    
# Prompt Player 2 for their move
    
# Check if Player 2 has won or if there is a tie
