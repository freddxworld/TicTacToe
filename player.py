#this will take hold of the player
class Player:
    def __init__(self):
        self.taken_spot = True
    def playerChoice(self, board):
        from game import Game
        self.board = board
        game_func = Game(self.board)
        while self.taken_spot:
            row = self.get_valid_row()
            col = self.get_valid_col()
            if game_func.is_spot_empty(row, col):
                print("player chooses (" + str(row) + "," + str(col) + ")\n")
                self.board[row][col] = 'X'
                print("\n----------------------------------------------------------------- \n")
                break
            else:
                print("that is spot is taken please choose another\n")
                print("\n----------------------------------------------------------------- \n")
    def get_valid_row(self):
        while True:
            user_input = input("choose row: ")
            if user_input.isdigit() and int(user_input) < 3:
                return int(user_input)
            else:
                print("invalid input please try again")
    def get_valid_col(self):
        while True:
            user_input = input("choose col: ")
            if user_input.isdigit() and int(user_input) < 3:
                return int(user_input)
            else:
                print("invalid input please try again")
    