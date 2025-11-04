import curses
from curses import wrapper

class window:
  def __init__(self,height,width,y,x):
    self.win = curses.newwin(height,width,y,x)
    self.height = height
    self.width = width
    self.y = y
    self.x = x
  def set_cursor(self,y,x):
    self.win.move(y,x)
  def draw_text(self,text):
    self.win.addstr(text)
  def draw_text_refresh(self,text):
    self.win.addstr(text)
    self.win.refresh()

def main(stdscr):
  stdscr.clear()

  win1 = window(10,10,10,10)
  win1.set_cursor(1,1)
  win1.draw_text_refresh("welcome aboard")
  
  stdscr.refresh()
  stdscr.getch()

wrapper(main)
