#this class will take charge of the AI/minmax algorithm
import random

class PlayerAI:
    def __init__(self): 
        self.taken_spot = True
        from game import Game
        self.board = Game.board

    #will evaluate on how the board is going so far, so it checks if someone has won or not or if there is a draw
    def eval(self, board):
        pass
    #mimimax algorithm
    def minimax(self, board, depth, is_maximizing):
        pass
    #will call upon the minimax algorithm to find the best move
    def find_best_move(self, board):
        pass
    def computer_choice(self, board):

        from game import Game
        game_func = Game(board)
 
        max_eval = float('-inf')
        move = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = self.minimax(board, 0, False)
                    board[i][j] = ' '
                    if eval > max_eval:
                        max_eval = eval
                        move = (i, j)


        if game_func.is_spot_empty(move[0], move[1]):
            print("computer chooses (" + str(move[0]) + "," + str(move[1]) + ")\n")
            self.board[move[0]][move[1]] = 'O'
            print("\n----------------------------------------------------------------- \n")
"""
 Function to check if the current player has won
def check_winner(board, player):
    # Check rows
    for row in board:
        if row.count(player) == 3:
            return True
    # Check columns
    for col in range(3):
        if [board[row][col] for row in range(3)].count(player) == 3:
            return True
    # Check diagonals
    if [board[i][i] for i in range(3)].count(player) == 3 or [board[i][2-i] for i in range(3)].count(player) == 3:
        return True
    return False

# Function to check if the board is full
def is_full(board):
    return sum(row.count(' ') for row in board) == 0

# Function to evaluate the current state of the board
def evaluate(board):
    if check_winner(board, 'X'):
        return -1
    elif check_winner(board, 'O'):
        return 1
    elif is_full(board):
        return 0
    else:
        return None

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    score = evaluate(board)

    if score is not None:
        return score

    if is_maximizing:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth+1, False)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth+1, True)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
        return min_eval

"""