from Sudoku import Game


def main():
    sudoku = """145327698
                839654127
                672918543
                496185372
                218473956
                753296481
                367542819
                984761235
                521839764"""

    board = list([[int(i) for i in line] for line in sudoku.split()])

    sudoku = Game(board)
    sudoku.printBoard()
    print(sudoku.solved())


if __name__ == "__main__":
    main()
