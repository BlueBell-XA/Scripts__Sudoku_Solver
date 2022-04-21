"""This Module handles reading, formatting and writing Sudoku puzzles"""


def read_file(txt_doc: str) -> list:
    """Read a given text file of Sudoku puzzles and return a 3D list."""

    column, row = 1, 1
    sudoku_row = []
    sudoku_puzzle = []
    sudoku_puzzle_list = []

    # Open the file and iterate through each character in file.
    with open(txt_doc, 'r', encoding='UTF8') as file:
        while True:
            char = file.read(1)

            # Finalise any unfinished rows/puzzles and break the loop
            if not char:
                if len(sudoku_row) > 0:
                    sudoku_puzzle.append(sudoku_row)
                if len(sudoku_puzzle) > 0:
                    sudoku_puzzle_list.append(sudoku_puzzle)
                break

            # Add each character into the row list
            if char != '\n':
                sudoku_row.append(int(char))
                column += 1

            # Add a completed row into the current puzzle and reset the row
            elif char == '\n' and column == 10:
                sudoku_puzzle.append(sudoku_row)
                sudoku_row = []
                column = 1
                row += 1

            # Add the completed puzzle to the list and reset the puzzle
            elif char == '\n' and row > 1:
                sudoku_puzzle_list.append(sudoku_puzzle)
                sudoku_puzzle = []
                row = 1

    file.close()
    return sudoku_puzzle_list


def __format_board(sudoku_list: list) -> str:
    """Formats a given list of Sudokus into a human readable String."""

    complete_string = ""

    # Iterate through every puzzle and format for human readability.
    # Each value/line is appended to the complete_string prior to returning.
    for puzzle in range(len(sudoku_list)):
        for row in range(9):
            for col in range(9):
                complete_string = complete_string + str(sudoku_list[puzzle][row][col]) + " "
                if col in (2, 5):
                    complete_string += "| "
            complete_string += '\n'
            if row in (2, 5):
                complete_string += "------+-------+------\n"
        complete_string += "\n\n"

    return complete_string


def write_results(sudoku_list):
    """Takes a list of Sudokus and writes their formatted version to file"""

    with open("completed_puzzles.txt", 'w', encoding='UTF8') as file:
        file.write(__format_board(sudoku_list))

    file.close()
