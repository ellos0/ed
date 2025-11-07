import curses

import line
import window
from window import Window

def main(stdscr):
    stdscr.clear()
    curses.curs_set(1) # make cursor visible

    win = Window(10, 40, 2, 2)
    
    line.set_cursor_n(win,[1,1])
    line.insert_text(win, "hello ")
    line.set_cursor_n(win, [7,1])
    line.insert_text(win, "world!")

    window.cursor(win)
    window.box(win)

    stdscr.refresh()
    window.refresh(win)

    stdscr.getch()

curses.wrapper(main)
