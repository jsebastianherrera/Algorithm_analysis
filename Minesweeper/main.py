from random import randint
PATH = 'board.txt'


def read_file(path: str):
    board = []
    with open(path, 'r') as f:
        lines = f.readlines()
        line = lines.pop(0)
        tokens = line.strip().split(' ')
        w, h = int(tokens[0].strip()), int(tokens[1].strip())
        board = [[0 for i in range(w)] for j in range(h)]
        mines = []
        i = 0
        for line in lines:
            tokens = line.strip().split(' ')
            j = 0
            for token in tokens:
                board[i][j] = token
                if token == 'X':
                    mines.append((i, j))
                j += 1
            i += 1
    return board, mines


class Board:
    def __init__(self, board: list(list()), mines: list):
        self.rows = len(board)
        self.cols = len(board[0])
        self._fullBoard = board
        self.board = [['X' for i in range(self.rows)]
                      for j in range(self.cols)]
        self.mines = mines
        self._possibleMines = []

    def print(self):
        for i in range(self.rows):
            print('')
            for j in range(self.cols):
                print(' ', self.board[i][j], end='\t')
        print('')

    def _isValidPos(self, i, j, n, m):
        if (i < 0 or j < 0 or i > n - 1 or j > m - 1):
            return 0
        return 1

    def _proba(self, current: tuple()):
        i, j = current[0], [1]
        adjacents = self._getAdjacents(i, j)

    def clicked(self, i: int, j: int):
        if (i, j) in self.mines:
            print('Boom')
            exit(1)
        self.board[i][j] = self._fullBoard[i][j]
        self.print()

    def _getAdjacents(self, i: int, j: int) -> list(tuple()):
        v = []
        n, m = len(self.board), len(self.board[0])
        if (self._isValidPos(i - 1, j - 1, n, m)):
            v.append((i - 1, j - 1))
        if (self._isValidPos(i - 1, j, n, m)):
            v.append((i - 1, j))
        if (self._isValidPos(i - 1, j + 1, n, m)):
            v.append((i - 1, j + 1))
        if (self._isValidPos(i, j - 1, n, m)):
            v.append((i, j - 1))
        if (self._isValidPos(i, j + 1, n, m)):
            v.append((i, j + 1))
        if (self._isValidPos(i + 1, j - 1, n, m)):
            v.append((i + 1, j - 1))
        if (self._isValidPos(i + 1, j, n, m)):
            v.append((i + 1, j))
        if (self._isValidPos(i + 1, j + 1, n, m)):
            v.append((i + 1, j + 1))
        return v


if __name__ == '__main__':
    b, m = read_file(PATH)
    board = Board(b, m)
    board.print()
    # First move
    i, j = randint(0, board.rows-1), randint(0, board.cols-1)
    board.clicked(i, j)
