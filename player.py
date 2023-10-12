#this will take hold of the player
class Player:
    def __init__(self):
        self.taken_spot = True
    def playerChoice(self, board):
        from game import Game
        self.board = board
        game_func = Game(self.board)
        while self.taken_spot:
            row = int(input("choose row: "))
            col = int(input("choose column: "))
            if game_func.is_spot_empty(row, col):
                print("player chooses (" + str(row) + "," + str(col) + ")\n")
                self.board[row][col] = 'X'
                print("\n----------------------------------------------------------------- \n")
                break
            else:
                print("that is spot is taken please choose another\n")
                print("\n----------------------------------------------------------------- \n")