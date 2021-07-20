import sys
import math
import matplotlib.pyplot as plt
import random

import numpy as np
from scipy.interpolate import make_interp_spline, BSpline

""" Find the longest increasing subsequence in the list a

    Returns a list s such that [a[s[i]] for i in range(lens(s))] is
    a longest increasing subsequence of a.
"""
def lis(a):
    n = len(a)
    # b[i] = length of lis in b[:i] that includes i
    # p[i] = index of second-last element of lis in b[:i] that includes i
    b = [None]*n
    p = [None]*n
    for i in range(n):
        b[i] = 1
        for j in range(i):
            if a[j] < a[i] and b[j]+1 > b[i]:
                b[i] = b[j]+1
                p[i] = j
    m = max(b)
    imax = b.index(m)
    s = list()
    for j in range(m):
        s.append(imax)
        imax = p[imax]
    return s[::-1]

def range_filter(x, a, b, inf):
    if a <= x and x < b:
        return x
    return inf

def contiguous_lis(a, r):
    n = len(a)
    s = []
    inf = float('inf')
    for i in range(n-r):
        ap = [range_filter(x, i, i+r, inf) for x in a]
        # print(ap)
        sp = lis(ap)
        if ap[sp[-1]] == inf:
            sp.pop(-1)
        if len(sp) > len(s):
            s = sp
    return s

# test code for lis
def list_test():
    a = list(range(40))
    random.shuffle(a)
    print(a)
    l = lis(a)
    print(l)
    print([a[i] for i in l])

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

def flip_order(a):
    n = len(a)
    if n <= 2:
        return a
    return flip_order(a[:n//2]) + flip_order(a[-1:n//2-1:-1])

""" This produces the same result as repeated calls to blow_up([0,1,2,3]) """
def double_flip_order(a):
    n = len(a)
    if n == 0 or n % 4 != 0:
        return a
    # order = [1, 0, 3, 2]
    order = [2, 0, 3, 1]
    rev = [1, -1, 1, -1]
    subarrays = [ a[i*n//4:(i+1)*n//4] for i in range(4) ]
    return sum([double_flip_order(subarrays[order[i]][::rev[order[i]]]) \
                for i in range(4)], [])

""" invert a permuation a:[0,...,n] -> [0,...,n] """
def invert(a):
    inverter = sorted([(a[i], i) for i in range(len(a))])
    return [x[1] for x in inverter]

def rainbow(n):
    return [(i, n-i-1) for i in range(n//2)]

def twist(n):
    return [(i, n//2+i) for i in range(n//2)]

def hypercube(n):
    if n == 1:
        return []
    halfn = n//2
    h0 = hypercube(halfn)
    h1 = [(t[0]+halfn, t[1]+halfn) for t in h0]
    return h0 + h1 + rainbow(n)

def skiplist(n):
    g = list()
    s = 2
    while s < n:
        r = rainbow(s)
        print("len(r)= {}".format(len(r)))
        for p in range(0, n, s//2):
            g.extend([(x[0]+p,(x[1]+p)%n) for x in r])
        s *= 2
    return g

def alon_roitman_p2(n):
    halfn = n // 2
    g = [(i,n-i-1) for i in range(halfn)]
    g = list()
    s = 1
    while s < 2:
        g.extend([(i,halfn + (s-i)%halfn) for i in range(halfn)])
        s *= 2
    return g

def alon_roitman(n, d=None):
    if d is None:
        d = int(math.log(n, 2))
    g = list()
    halfn = n//2
    for i in range(d):
        s = random.randrange(halfn)
        g.extend([(i,halfn + (s-i)%halfn) for i in range(halfn)])
        # s = random.randrange(halfn)
        # g.extend([((s-i)%halfn, halfn+i) for i in range(halfn)])
    return g

def draw_arc(x0, x1, c = "black", lw=0.25):
    if x0 == x1:
        return
    x0, x1 = min(x0, x1), max(x0, x1)
    res = 100 # resolution for approximating a curve with lines
    xs = [x0+i*(x1-x0)/res for i in range(res+1)]
    ys = [math.sin(math.pi*(x-x0)/(x1-x0))*0.7*(x1-x0) for x in xs]
    plt.plot(xs, ys, color=c, lw=lw)


def max_rainbow(g, a):
    m = len(g)
    edges = [(min(a[e[0]], a[e[1]]), max(a[e[0]], a[e[1]])) for e in g]
    lensperm = sorted(list(range(m)), key=lambda i: edges[i][0]-edges[i][1])
    b = [None] * m
    p = [None] * m
    for k in range(m):
        i = lensperm[k]
        v, w = edges[i]
        b[i] = 1
        for k2 in range(k):
            j = lensperm[k2]
            x, y = edges[j]
            if x < v and w < y and b[j] + 1 > b[i]:
                b[i] = b[j]+1
                p[i] = j
    mx = max(b)
    imax = random.choice([i for i in range(m) if b[i] == mx])
    s = list()
    while imax is not None:
        s.append(imax)
        imax = p[imax]
    return [g[x] for x in s]


""" Return the parity of the number of one bits of n """
def parity(n):
    p = 0
    while n != 0:
        if n % 2:
            p = 1-p
        n //= 2
    return p

def parity_split(a):
    return [x for x in a if parity(x) == 0] + [x for x in a if parity(x) == 1]

def odd_even_split(a):
    return [x for x in a if x%2] + [x for x in a if not x%2]

if __name__ == "__main__":
    #random.seed(0)   # for reproducibility
    d = 3
    if len(sys.argv) == 2:
        d = int(sys.argv[1])

    # a = [0]
    # for _ in range(d):
    #     a = blow_up(a)

    a = list(range(2**d))
    # a = parity_split(a)
    # print(a)
    a = double_flip_order(a)
    # print(a)
    # a = odd_even_split(a)
    # print(a)
    # a = list(range(2**d))
    # a = list(range(2**d))
    # print(a)
    # a = list(range(4**d))
    # a = list(range(4**d // 2))
    # a += [4**d-x-1 for x in a]
    ainv = invert(a)

    plt.plot(a)
    n = len(a)
    print("n = {}".format(len(a)))
    s = lis(a)
    print("LIS has length {}".format(len(lis(a))))
    print(s)
    # r = 2**d
    # c = contiguous_lis(a, r)
    # print("Longest {}-contiguous IS has length {}".format(r, len(c)))
    # print(c)
    # print([a[x] for x in c])
    # g = hypercube(n)
    # g = skiplist(n)
    # g = alon_roitman(n, 1)
    # for g, c in [(skiplist(n), "black"), (hypercube(n), "red")]:
    # for g, c in [([(i, (i+1)%n) for i in range(n)], "black")]: \
    g = hypercube(n) + alon_roitman(n)
    random.shuffle(g)
    c = "red"
    # for g, c in [(alon_roitman(n)+hypercube(n), "red")]:
    for (y0, y1) in g:
        x0 = ainv[y0]
        x1 = ainv[y1]
        draw_arc(x0, x1, c)
    r = max_rainbow(g, ainv)
    print("largest rainbow size is {}".format(len(r)))
    for (y0, y1) in r:
        x0 = ainv[y0]
        x1 = ainv[y1]
        draw_arc(x0, x1, "green", 2)
    plt.xlabel("i")
    plt.ylabel("pi[i]")
    plt.show()
