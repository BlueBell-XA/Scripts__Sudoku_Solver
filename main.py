"""This Module handles the actual solving of the Sudoku puzzles"""
from time import time
import sys
import file_handler

# Global variables/constants
TIMEOUT_SECONDS = 10
sudoku_list = file_handler.read_file("blank puzzles.txt")
start_timer: float


def solve(puzzle):
    """Recursively try each number possibility and back-track if required until puzzle is solved"""

    # Check time elapsed on each recursion.
    # Returns the current puzzle solving progress with a messaged attached.
    if time()-start_timer >= TIMEOUT_SECONDS:
        puzzle.append(["***The above Sudoku could not be completed in a reasonable time frame***"])
        return puzzle

    # Retrieve the x-y co-ordinates of the next empty cell.
    # If no empty cells, return the completed puzzle.
    empty_cell = find_empty(puzzle)
    if not empty_cell:
        return puzzle
    row, column = empty_cell

    # Iterate through values 1-9 of a given cell and sets a valid number.
    for number in range(1, 10):
        if is_valid_number(puzzle, number, (row, column)):
            puzzle[row][column] = number

            # Recursion happens here WHILE still in 'for' loop.
            if solve(puzzle):
                return puzzle

        # Reset current position.
        # Due to the recursion happening in the 'for' loop, program will 'back-track' to previous numbers
        # and continue to increment the loop and begin new recursion until a full solution is found.
        puzzle[row][column] = 0

    return False


def find_empty(puzzle):
    """Look through entire board to find the next empty cell"""

    for row in range(9):
        for column in range(9):
            if puzzle[row][column] == 0:
                return (row, column)

    return None


def is_valid_number(puzzle: list, number: int, position: list) -> bool:
    """Check whether or not a proposed number is valid in a position"""

    # Check if number is in row, ignoring the current position
    for column in range(9):
        if puzzle[position[0]][column] == number and position[1] != column:
            return False

    # Check if number is in column, ignoring the current position
    for row in range(9):
        if puzzle[row][position[1]] == number and position[0] != row:
            return False

    # Check if number is in current box, ignoring the current position
    box_x = position[1] // 3
    box_y = position[0] // 3
    try:
        for row in range(box_y * 3, box_y * 3 + 3):
            for column in range(box_x * 3, box_x * 3 + 3):
                if puzzle[row][column] == number and (row, column) != position:
                    return False
    except IndexError:
        print("A Sudoku puzzle is incorrectly sized. Exiting now!")
        sys.exit()

    return True


# Iterate through each Sudoku puzzle and solve them.
# A timer is reset for each puzzle to prevent long run-times.
for i in range(len(sudoku_list)):
    start_timer = time()
    solve(sudoku_list[i])
file_handler.write_results(sudoku_list)
