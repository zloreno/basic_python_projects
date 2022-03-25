import curses
from curses import color_pair, wrapper
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


def main(stdscr):
    # Define color settings
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    blue_and_black = curses.color_pair(1)

    stdscr.clear()
    # Use color settings to the string
    stdscr.addstr(5, 0, 'Hello World!', blue_and_black)
    stdscr.refresh()
    stdscr.getch()


wrapper(main)
