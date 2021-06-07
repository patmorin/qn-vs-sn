#!/usr/bin/python3

import sys
import random


def graph(n, d):
    edges = list()
    for _ in range(d):
        r = random.randrange(n)
        edges.extend([(i, r-i) for i in range(r//2)])
        edges.extend([(i, r-i-1) for i in range(r//2)])
        edges.extend([(r+i, n-i) for i in range(1, (n-r)//2)])
        edges.extend([(r+i, n-i-1) for i in range(1, (n-r)//2)])
    return edges

def dot_output(edges):
    print("graph{")
    for v,w in edges:
        print(" {} -- {};".format(v, w))
    print("}")


if __name__ == "__main__":
    random.seed(0)
    n = 23
    d = 4
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    if len(sys.argv) > 2:
        d = int(sys.argv[2])
    dot_output(graph(n, d))
