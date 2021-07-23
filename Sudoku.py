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

    def isSolved(self) -> bool:
        grid = self.matrix
        for i in range(9):
            j, k = (i // 3) * 3, (i % 3) * 3
            if len(set(grid[i, :])) != 9 or len(set(grid[:, i])) != 9\
                    or len(set(grid[j:j+3, k:k+3].ravel())) != 9:
                return False
        return True

    def printBoard(self):
        print(self)

    def solve(self):

        def safeToInsert(grid, row, col, num):
            for x in range(9):
                if grid[row][x] == num:
                    return False
            for x in range(9):
                if grid[x][col] == num:
                    return False

            startRow = row - row % 3
            startCol = col - col % 3

            for i in range(3):
                for j in range(3):
                    if grid[i + startRow][j + startCol] == num:
                        return False

            return True

        def backtrack(grid, row, col):

            if (row == 8 and col == 9):
                return True

            if col == 9:
                row += 1
                col = 0

            if grid[row][col] > 0:
                return backtrack(grid, row, col + 1)

            for num in range(1, 10, 1):
                if safeToInsert(grid, row, col, num):
                    grid[row][col] = num

                    if backtrack(grid, row, col + 1):
                        return True

                grid[row][col] = 0

            return False

        if backtrack(self.matrix, 0, 0):
            self.printBoard()
        else:
            print('Solution doesnt exist')
