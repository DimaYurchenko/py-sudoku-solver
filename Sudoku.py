import numpy as np


class Game:
    def __init__(self, matrix):
        self.matrix = np.array(matrix)

    def __str__(self) -> str:
        string = ''

        for i in range(9):
            for j in range(9):
                if j in [3, 6]:
                    string += '|  '
                string += ('_' if self.matrix[i][j] ==
                           0 else str(self.matrix[i][j])) + '  '
            if i in [2, 5]:
                string += '\n--------------------------------'
            string += '\n'
        return string

    def solved(self) -> bool:
        grid = self.matrix
        for i in range(9):
            j, k = (i // 3) * 3, (i % 3) * 3
            if len(set(grid[i, :])) != 9 or len(set(grid[:, i])) != 9\
                    or len(set(grid[j:j+3, k:k+3].ravel())) != 9:
                return False
        return True

    def printBoard(self):
        print(self)
