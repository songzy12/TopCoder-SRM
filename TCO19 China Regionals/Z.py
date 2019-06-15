w, h = map(int, input().split())
x, y = map(int, input().split())
r = int(input())
import math
r = r / 180.0 * math.pi

# 斜率需要是有理数
# 因为角度都是整数
# 所以只需要检查四个角度

def step(w, h, x, y, r):
    up_t = (h-y)/math.sin(r)
    if up_t >= 0:
        up_x = x + up_t * math.cos(r)
        if 0 <= up_x <= w:
            return (w, h)

    down_t = -y/math.sin(r)
    if down_t >= 0:
        down_x = x + down_t * math.cos(r)
        if 0 <= down_x <= w:
            return (w, 0)

    left_t = -x / math.cos(r)
    if left_t >= 0:
        left_y = y + left_t * math.sin(r)
        if 0 <= left_y <= h:
            return (0, left_y)


def solve(w, h, x, y, r):

    if r == 0 or r == 180:
        return y == 0 or y == h
    if r == 90 or r == 270:
        return x == 0 or x == w
