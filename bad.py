import sys
import math
import matplotlib.pyplot as plt
import random

import numpy as np
from scipy.interpolate import make_interp_spline, BSpline


def blow_up(a):
    c = list()
    fwd = [1, 0, 3, 2]
    rev = fwd[::-1]
    map = [fwd, rev, fwd, rev]
    # map = [fwd] * 4
    for x in a:
        basic = map[x % 4]
        c.extend([4*x + basic[i] for i in range(4)])
    return c

def invert(a):
    inverter = sorted([(a[i], i) for i in range(len(a))])
    return [x[1] for x in inverter]

def rainbow(n):
    return [(i, n-i-1) for i in range(n//2)]

def hypercube(n):
    if n == 1:
        return []
    halfn = n//2
    h0 = hypercube(halfn)
    h1 = [(t[0]+halfn, t[1]+halfn) for t in h0]
    return h0 + h1 + rainbow(n)


def alon_roitman(n, d):
    g = list()
    halfn = n//2
    for i in range(d):
        s = random.randrange(halfn)
        # s = 100
        g.extend([(i,halfn + (s-i)%halfn) for i in range(halfn)])
    # g += [(n-i-1, n-j-1) for (i,j) in g]
    return g

def draw_arc(x0, x1):
    if x0 == x1:
        return
    x0, x1 = min(x0, x1), max(x0, x1)
    res = 100
    xs = [x0+i*(x1-x0)/res for i in range(res+1)]
    ys = [math.sin(math.pi*(x-x0)/(x1-x0))*0.7*(x1-x0) for x in xs]
    plt.plot(xs, ys, color="black", lw=0.25)


    # plt.plot([x0, xp, x1], [0, (max(x0,x1)-min(x0,x1))/4, 0], color="black")

if __name__ == "__main__":
    #random.seed(0)   # for reproducibility
    d = 3
    if len(sys.argv) == 2:
        d = int(sys.argv[1])

    a = [0]
    for _ in range(d):
        a = blow_up(a)
    ainv = invert(a)

    plt.plot(a)
    n = len(a)
    print("max = {}, min = {}, n = {}".format(max(a), min(a), len(a)))
    g = hypercube(n)
    g = alon_roitman(n, 1)
    for (y0, y1) in g:
        x0 = ainv[y0]
        x1 = ainv[y1]
        draw_arc(x0, x1)
    plt.xlabel("i")
    plt.ylabel("pi[i]")
    plt.show()


# Revolution skin neck area , heartworm protection , ear mites , fleas , ticks
# W
