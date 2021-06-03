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

def matching(a, b):
    n = len(a)
    assert(n == len(b))
    return [(a[i], b[i]) for i in range(n)]


def graph(n, d):
    edges = list()
    a = list(range(n))
    b = [x+n for x in a]
    c = [x+2*n for x in a]
    edges.extend(matching(a,b))
    edges.extend(matching(b,c))
    edges.extend(expander(a, c[::-1], d))
    return edges

def dot_output(edges):
    print("graph{")
    for v,w in edges:
        print(" {} -- {};".format(v, w))
    print("}")


if __name__ == "__main__":
    n = 23
    d = 4
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    if len(sys.argv) > 2:
        d = int(sys.argv[2])
    dot_output(graph(n, d))
