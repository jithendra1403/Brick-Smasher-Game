from numpy import genfromtxt
from brick import Brick
from config import BRICK_SIZE



def cursor_to_top():
    print("\033[0;0H")


def log(s):
    with open("a.txt", "a") as f:
        f.write(s)


def get_bricks(width, height, level) -> [Brick]:
    data = []
    if level == 1:
        data = genfromtxt('brick_pattern.csv', delimiter=',')
    if level == 2:
        data = genfromtxt('brick_pattern2.csv', delimiter=',')
    if level == 3:
        data = genfromtxt('brick_pattern2.csv', delimiter=',')
    bricks = []
    for line in data:
        new_brick = Brick(max_width=width, max_height=height, strength=int(line[-1]),
                          y=int(line[0]), x=int(line[1] * BRICK_SIZE), size=BRICK_SIZE)
        bricks.append(new_brick)
    return bricks



