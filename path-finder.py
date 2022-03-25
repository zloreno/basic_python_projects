# define queu as only the path, not the pos, path
import curses
from curses import wrapper
import queue
import time

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]


def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j

    return None


def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    # Draw the maze into the terminal
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j*2, 'X', RED)
            else:
                stdscr.addstr(i, j*2, value, BLUE)

    bottom_text = f'path: {path}'
    bottom_row = len(maze) + 1
    stdscr.addstr(bottom_row, 0, bottom_text, BLUE)


def append_if_valid(maze, input_row, input_column, nb):
    if maze[input_row][input_column] != '#':
        nb.append((input_row, input_column))
    return nb


def find_nb(maze, row, col):
    nb = []
    if row > 0:  # Up
        nb = append_if_valid(maze, input_row=row - 1, input_column=col, nb=nb)
    if row + 1 < len(maze):  # Down
        nb = append_if_valid(maze, input_row=row + 1, input_column=col, nb=nb)
    if col > 0:  # Left
        nb = append_if_valid(maze, input_row=row, input_column=col - 1, nb=nb)
    if col + 1 < len(maze[0]):  # Right
        nb = append_if_valid(maze, input_row=row, input_column=col + 1, nb=nb)

    return nb


def find_path(maze, stdscr):
    start = 'O'
    end = 'X'
    start_pos = find_start(maze, start)

    q = queue.Queue()
    # add to the queue the position and the path that lead to said position
    q.put((start_pos, [start_pos]))

    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.2)
        stdscr.refresh()

        if maze[row][col] == end:
            return path

        nbs = find_nb(maze, row, col)
        for nb in nbs:
            if nb in visited:
                continue

            new_path = path + [nb]
            q.put((nb, new_path))
            visited.add(nb)


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    find_path(maze, stdscr)
    stdscr.getch()


wrapper(main)
