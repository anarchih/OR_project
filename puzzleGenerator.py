from copy import deepcopy
from random import random


def swap(a, q, w):
    a[q[0]][q[1]], a[w[0]][w[1]] = a[w[0]][w[1]], a[q[0]][q[1]]
    q[0] = w[0]
    q[1] = w[1]


def puzGen(goal, width, height):
    p = [int(random() * width), int(random() * height)]
    t = deepcopy(goal)
    i = 0
    while i <= 1000 or p != [width - 1, height - 1]:
        a = int(random() * 4)
        if a == 0 and p[0] - 1 >= 0:
            swap(t, p, [p[0] - 1, p[1]])
        elif a == 1 and p[1] - 1 >= 0:
            swap(t, p, [p[0], p[1] - 1])
        elif a == 2 and p[0] + 1 < width:
            swap(t, p, [p[0] + 1, p[1]])
        elif a == 3 and p[1] + 1 < height:
            swap(t, p, [p[0], p[1] + 1])
        else:
            i -= 1
        i += 1
    return t


def main():
    g = [[0, 1, 2, 3],
         [0, 1, 2, 3],
         [0, 1, 2, 3],
         [0, 1, 2, 3]]
    q = puzGen(g, 4, 4)
    print(q)

if __name__ == '__main__':
    main()
