import curses
from curses import wrapper

def main(stdscr):
  stdscr.clear()
  
  stdscr.addstr("welcome to my text editor!")

  stdscr.refresh()
  stdscr.getch()

wrapper(main)
