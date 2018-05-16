class SeaFallPlayerRandom:
    def __init__(self, game):
        self.game = game

    def play(self, board):
        a = np.random.randint(self.game.getActionSize())

        valids = self.game.getValidMoves(board, 1)

        while valids[a] != 1:
            a = np.random.randint(self.game.getActionSize())
        return a

class SeaFallPlayerHuman:
    def __init__(self, game):
        self.game = game

    def play(self, board):
        a = np.random.randint(self.game.getActionSize())

        valids = self.game.getValidMoves(board, 1)

        while True:
            move = int(input())
            if valid_moves[move]: break
            else: print('Invalid move')
        return move
