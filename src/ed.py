import curses
from curses import wrapper

class Window:
  def __init__(self,height,width,y,x):
    self.height = height
    self.width = width
    self.y = y
    self.x = x
    self.win = curses.newwin(height,width,y,x)
  def box(self):
    self.win.box()
  def refresh(self):
    self.win.refresh()
  def write(self,y,x,text):
    self.win.addstr(y,x,text)

def main(stdscr):
  stdscr.clear()
  win = Window(10,40,2,2)

  win.write(1,1,"hello")
  win.box()
  
  stdscr.refresh()
  win.refresh()

  stdscr.getch()
  
wrapper(main)
