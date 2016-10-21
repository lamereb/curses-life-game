import random, curses

def build_empty_world(size):
  world = []
  for i in range(size):
    world.append([])
    for k in range(size):
      world[i].append(False)
  return world


def random_world(size):
  world = build_empty_world(size)
  for i in range(size):
    for k in range(size):
      gen = random.randint(0, 10)
      if gen > 7:
        world[i][k] = True
  return world


def growth_world(s, start_y, start_x, size):
  mid_y, mid_x = s.getmaxyx()
  x = start_x + int(mid_x / 2)
  y = start_y + int(mid_y / 3)
  world = build_empty_world(size)
  world[y + 1][x + 1] = True 
  world[y + 2][x + 1] = True
  world[y + 3][x + 1] = True
  world[y + 5][x + 1] = True
  world[y + 1][x + 2] = True
  world[y + 4][x + 3] = True
  world[y + 5][x + 3] = True
  world[y + 2][x + 4] = True
  world[y + 3][x + 4] = True
  world[y + 5][x + 4] = True
  world[y + 1][x + 5] = True
  world[y + 5][x + 5] = True
  return world


def diamond_terminus(s, start_y, start_x, size):
  mid_y, mid_x = s.getmaxyx()
  x = start_x + int(mid_x / 2)
  y = start_y + int(mid_y / 3)
  world = build_empty_world(size)
  world[y + 1][x + 2] = True 
  world[y + 1][x + 3] = True
  world[y + 1][x + 5] = True
  world[y + 2][x + 1] = True
  world[y + 3][x + 4] = True
  world[y + 3][x + 5] = True
  world[y + 4][x + 2] = True
  world[y + 4][x + 3] = True
  world[y + 4][x + 5] = True
  world[y + 5][x + 1] = True
  world[y + 5][x + 3] = True
  world[y + 5][x + 5] = True
  return world

def gospers_glider_gun(s, start_y, start_x, size):
  mid_y, mid_x = s.getmaxyx()
  x = start_x + int(mid_x / 3)
  y = start_y + int(mid_y / 4)
  world = build_empty_world(size)
  world[y + 6][x + 2] = True
  world[y + 7][x + 2] = True
  world[y + 6][x + 3] = True
  world[y + 7][x + 3] = True
  world[y + 6][x + 12] = True
  world[y + 7][x + 12] = True
  world[y + 8][x + 12] = True
  world[y + 6][x + 18] = True
  world[y + 7][x + 18] = True
  world[y + 8][x + 18] = True
  world[y + 5][x + 13] = True
  world[y + 9][x + 13] = True
  world[y + 5][x + 17] = True
  world[y + 9][x + 17] = True
  world[y + 4][x + 14] = True
  world[y + 10][x + 14] = True

  world[y + 4][x + 15] = True
  world[y + 10][x + 15] = True
  world[y + 7][x + 16] = True
  world[y + 7][x + 19] = True

  world[y + 4][x + 22] = True
  world[y + 5][x + 22] = True
  world[y + 6][x + 22] = True
  world[y + 4][x + 23] = True
  world[y + 5][x + 23] = True
  world[y + 6][x + 23] = True

  world[y + 3][x + 24] = True
  world[y + 7][x + 24] = True
  world[y + 2][x + 26] = True
  world[y + 3][x + 26] = True
  world[y + 7][x + 26] = True
  world[y + 8][x + 26] = True
  world[y + 4][x + 36] = True
  world[y + 5][x + 36] = True
  world[y + 4][x + 37] = True
  world[y + 5][x + 37] = True
  return world


def growth_world_2(s, start_x, start_y, size):
  mid_y, mid_x = s.getmaxyx()
  x = start_x + int(mid_x / 3)
  y = start_y + int(mid_y / 2)
  world = build_empty_world(size)
  # 2 to 9
  world[y][x + 2] = True
  world[y][x + 3] = True
  world[y][x + 4] = True
  world[y][x + 5] = True
  world[y][x + 6] = True
  world[y][x + 7] = True
  world[y][x + 8] = True
  world[y][x + 9] = True

  # 11 to 15
  world[y][x + 11] = True
  world[y][x + 12] = True
  world[y][x + 13] = True
  world[y][x + 14] = True
  world[y][x + 15] = True

  # 19 to 21
  world[y][x + 19] = True
  world[y][x + 20] = True
  world[y][x + 21] = True

  # 28 to 34
  world[y][x + 28] = True
  world[y][x + 29] = True
  world[y][x + 30] = True
  world[y][x + 31] = True
  world[y][x + 32] = True
  world[y][x + 33] = True
  world[y][x + 34] = True

  # 36 to 40
  world[y][x + 36] = True
  world[y][x + 37] = True
  world[y][x + 38] = True
  world[y][x + 39] = True
  world[y][x + 40] = True
  return world


def acorn(s, start_y, start_x, size):
  mid_y, mid_x = s.getmaxyx()
  x = start_x + int(mid_x / 2)
  y = start_y + int(mid_y / 3)
  world = build_empty_world(size)

  # 2,3  3,5  4,2  4,3  4,6  4,7  4,8
  world[y + 2][x + 3] = True
  world[y + 3][x + 5] = True
  world[y + 4][x + 2] = True
  world[y + 4][x + 3] = True
  world[y + 4][x + 6] = True
  world[y + 4][x + 7] = True
  world[y + 4][x + 8] = True
  return world


def r_pentimento(s, start_y, start_x, size):
  mid_y, mid_x = s.getmaxyx()
  x = start_x + int(mid_x / 2)
  y = start_y + int(mid_y / 2)
  world = build_empty_world(size)
  world[y + 2][x + 3] = True
  world[y + 2][x + 4] = True
  world[y + 3][x + 2] = True
  world[y + 3][x + 3] = True
  world[y + 4][x + 3] = True
  return world


def die_hard(s, start_y, start_x, size):
  mid_y, mid_x = s.getmaxyx()
  x = start_x + int(mid_x / 3)
  y = start_y + int(mid_y / 3)
  world = build_empty_world(size)
  world[y + 2][x + 8] = True
  world[y + 3][x + 2] = True
  world[y + 3][x + 3] = True
  world[y + 4][x + 3] = True
  world[y + 4][x + 7] = True
  world[y + 4][x + 8] = True
  world[y + 4][x + 9] = True
  return world


def some_pulsars(s, start_y, start_x, size):
  mid_y, mid_x = s.getmaxyx()
  x = start_x + int(mid_x / 3)
  y = start_y + int(mid_y / 4)
  world = build_empty_world(size)
  # blinker
  world[y + 3][x + 3] = True
  world[y + 4][x + 3] = True
  world[y + 5][x + 3] = True

  # toad
  y = y + 6;
  x = x + 10;
  world[y + 3][x + 3] = True
  world[y + 3][x + 4] = True
  world[y + 3][x + 5] = True

  world[y + 4][x + 2] = True
  world[y + 4][x + 3] = True
  world[y + 4][x + 4] = True

  # beacon
  x = x + 15;
  world[y + 2][x + 2] = True
  world[y + 2][x + 3] = True
  world[y + 3][x + 2] = True

  world[y + 4][x + 5] = True
  world[y + 5][x + 4] = True
  world[y + 5][x + 5] = True
  return world
