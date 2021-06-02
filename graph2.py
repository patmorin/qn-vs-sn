#!/usr/bin/python3

import random
import sys

def expander(a, b, d):
    n = len(a)
    assert(n == len(b))
    shifts = [0] + random.sample(range(2, n, 2), d-1)
    edges = list()
    for s in shifts:
        edges.extend([(a[i], b[(i+s)%n]) for i in range(n)])
        edges.extend([(a[i], b[(i+1+s)%n]) for i in range(n)])
    return edges


def graph(n, d):
    edges = [(i,i+1) for i in range(n-1)]
    edges.extend([(i, i+n) for i in range(n)])
    edges.extend([(i+n, i+2*n) for i in range(n)])
    edges.extend(expander(list(range(n)), list(range(3*n-1, 2*n-1, -1)), d))
    return edges

def dot_output(edges):
    print("graph{")
    for v,w in edges:
        print(" {} -- {};".format(v, w))


if __name__ == "__main__":
    n = 23
    d = 4
    if len(sys.args) > 1:
        n = int(args[1])
    if len(sys.args) > 2:
        d = int(args[2])
    dot_output(graph(n, d))
