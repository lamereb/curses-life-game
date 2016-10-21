#!/usr/bin/python
import curses, time, initialize


def destruct_scr(s):
  curses.nocbreak()
  s.keypad(0)
  curses.echo()
  curses.use_default_colors()
  curses.endwin()
  return 0


def display_main(s):
  s.clear()
  s.border(0)
  s.addstr(2, 2, "Conway's Game of Life")
  s.addstr(3, 2, "---------------------")
  s.addstr(5, 2, "Please pick a starting configuration. Pressing 'x' at any time will")
  s.addstr(6, 2, "return to this menu, and pressing j/k will increase/descrease speed")
  s.addstr(7, 2, "of regeneration. Arrow keys scroll around the world.")
  s.addstr(10, 4, "1. Random array")
  s.addstr(11, 4, "2. Growth state 1")
  s.addstr(12, 4, "3. Diamond Terminus")
  s.addstr(13, 4, "4. Gosper's Glider Gun")
  s.addstr(14, 4, "5. Growth state 2")
  s.addstr(15, 4, "6. Acorn")
  s.addstr(16, 4, "7. R-Pentomino")
  s.addstr(17, 4, "8. Die-Hard")
  s.addstr(18, 4, "9. Some Pulsars")
  s.addstr(21, 4, "x - To Exit")
  s.refresh()
  return s.getch()


def paint_world(s, world, start_y, start_x, win_y, win_x):
  c = '*'
  end_y = start_y + win_y - 1
  end_x = start_x + win_x - 1
  for i in range(start_y, end_y):
    for k in range(start_x, end_x):
      if world[i][k]:
        s.addch(i - start_y, k - start_x, c)


def copy_state_of(world):
  next_world = initialize.build_empty_world(len(world))
  for i in range(len(world)):
    for k in range(len(world)):
      next_world[i][k] = world[i][k]
  return next_world


def update_state_on(world):
  next_world = copy_state_of(world)
  for i in range(1, len(world) - 1):
    for k in range(1, len(world) - 1):
      count = 0
      # check cell's 8 neighbors
      if world[i - 1][k]:
        count += 1
      if world[i - 1][k - 1]:
        count += 1
      if world[i - 1][k + 1]:
        count += 1
      if world[i][k + 1]:
        count += 1
      if world[i][k - 1]:
        count += 1
      if world[i + 1][k]:
        count += 1
      if world[i + 1][k - 1]:
        count += 1
      if world[i + 1][k + 1]:
        count += 1
      if world[i][k]:
        if count <= 1:  # rule 1
          next_world[i][k] = False
        elif count > 3:
          next_world[i][k] = False
      elif count == 3 and world[i][k] == False:
        next_world[i][k] = True
      else:
        next_world[i][k] = world[i][k]
  return next_world


def start_life(s, init_state):
  WORLD_SIZE = 250
  ch  = ''
  start_x = 0; start_y = 0
  ms = 50.0

  if init_state == 1:
    this_world = initialize.random_world(WORLD_SIZE)
    ms = 10.0
  if init_state == 2:
    this_world = initialize.growth_world(s, start_y, start_x, WORLD_SIZE)
  if init_state == 3:
    this_world = initialize.diamond_terminus(s, start_y, start_x, WORLD_SIZE)
  if init_state == 4:
    this_world = initialize.gospers_glider_gun(s, start_y, start_x, WORLD_SIZE)
  if init_state == 5:
    this_world = initialize.growth_world_2(s, start_y, start_x, WORLD_SIZE)
  if init_state == 6:
    this_world = initialize.acorn(s, start_y, start_x, WORLD_SIZE)
  if init_state == 7:
    this_world = initialize.r_pentimento(s, start_y, start_x, WORLD_SIZE)
  if init_state == 8:
    this_world = initialize.die_hard(s, start_y, start_x, WORLD_SIZE)
  if init_state == 9:
    this_world = initialize.some_pulsars(s, start_y, start_x, WORLD_SIZE)
    
  s.nodelay(1)          # to stop blocking on getch()

  while ch != ord('x'):
    s.clear()

    win_y, win_x = s.getmaxyx()
    
    paint_world(s, this_world, start_y, start_x, win_y, win_x)
    next_world = update_state_on(this_world)
    time.sleep(ms / 1000.0)

    ch = s.getch()
    if ch != curses.ERR:

      # adjust speed and window_pane into world
      if ch == ord('k'):
        ms += 5.0
        if ms > 250.0:
          ms = 250.0
      elif ch == ord('j'):
        ms -= 5.0
        if ms < 5.0:
          ms = 5.0
      elif ch == curses.KEY_RIGHT:
        start_x += 1
        if (start_x + win_x) >= WORLD_SIZE:
          start_x = WORLD_SIZE - win_x 
      elif ch == curses.KEY_LEFT:
        start_x -= 1
        if start_x < 0:
          start_x = 0
      elif ch == curses.KEY_DOWN:
        start_y += 1
        if (start_y + win_y) >= WORLD_SIZE:
          start_y = WORLD_SIZE - win_y
      elif ch == curses.KEY_UP:
        start_y -= 1
        if start_y < 0:
          start_y = 0

    this_world = next_world
    curses.flushinp()   # flushing input buffer for key responsiveness 
    s.refresh()

  s.nodelay(0)          # restart blocking on getch
  return ch
 

def main(stdscr):
  curses.curs_set(0)
  ch = ''
  while ch != ord('x'):
    ch = display_main(stdscr)
    if ch >= ord('1') and ch <= ord('9'):
      start_life(stdscr, ch - 48)
  destruct_scr(stdscr)
  return 0


if __name__ == '__main__':
  curses.wrapper(main)

