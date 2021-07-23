from Sudoku import Game


def main():
    sudoku = """045327608
                830654127
                072918543
                496185372
                218470956
                050296481
                367542019
                984761235
                520839704"""

    board = list([[int(i) for i in line] for line in sudoku.split()])

    sudoku = Game(board)
    sudoku.solve()


if __name__ == "__main__":
    main()
