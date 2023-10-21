class PlayerAI:
    def __init__(self): 
        self.taken_spot = True

    #will evaluate on how the board is going so far, so it checks if someone has won or not or if there is a draw
    def eval(self, board):
        #were gonna import game fucntions from the game class
        from game import Game
        game_func = Game(board)
        #this checks if the player has won or if the computer has or if its a draw and based on that it returns a value
        if game_func.check_win('X'):
            return -1
        elif game_func.check_win('O'):
            return 1
        elif game_func.is_board_full():
            return 0
        else:
            return None

    #mimimax algorithm
    def minimax(self, board, depth, is_maximizing):
        #import some game fucntions that we will need
        from game import Game
        game_func = Game(board)
        #gets the score of the game board 
        score = self.eval(board)
        #if we have gotten a score then we return score and jump out of the the recursive
        if score is not None:
            return score
        #this will check ifs either the min(computer) or maximzing(player) turn
        if is_maximizing:
            #if its the player then we initalzie a max eval
            max_eval = float('-inf')
            #then we will go through the entire table and try all the possible empty spots to see what moves the player could do
            for i in range(3):
                for j in range(3):
                    #this will check if the spot that we are on is empty
                    if game_func.is_spot_empty(i,j):
                        #if its empty then we will put the O in the empty spot
                        board[i][j] = 'O'
                        #we then jump into the minimax function again starting the recursion
                        eval = self.minimax(board, depth+1, False)
                        #and we then reset the board spot to an empty spot
                        board[i][j] = ' '
                        #we then look for the max evaluation so which one is better
                        max_eval = max(max_eval, eval)
            #this will help us jump out of the recrusion
            return max_eval
        #we jump here if is_maximzing is false, meaning its the minmizing turn(computer)
        else:
            min_eval = float('inf')
            for i in range(3):
                for j in range(3):
                    if game_func.is_spot_empty(i,j):
                        board[i][j] = 'X'
                        eval = self.minimax(board, depth+1, True)
                        board[i][j] = ' '
                        min_eval = min(min_eval, eval)
            return min_eval

    #this will let the computer get its choice
    def computer_choice(self, board):
        #we import our variables and initalize variables that we will use
        from game import Game
        game_func = Game(board)
        max_eval = float('-inf')
        #will hold the computer move
        move = None
        #the rest of this will run the code for computer
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
            board[move[0]][move[1]] = 'O'
            print("\n----------------------------------------------------------------- \n")