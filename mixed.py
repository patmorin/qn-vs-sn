#!/usr/bin/python3

import sys
import random

def zigzag(n, i):
    edges = list()
    for j in range(n//2):
        edges.append(((i+j)%n, (i-j-1)%n))
        edges.append(((i+j+1)%n, (i-j-1)%n))
    return edges


def skipper(n, k):
    edges = list()
    for j in range(n):
        edges.append((j, (j+k)%n))
        edges.append(((j+1)%n, (j+k)%n))
    return edges

def graph(n, d):
    edges = [(i, (i+1)%n) for i in range(n)]
    for _ in range(d):
        edges.extend(zigzag(n, random.randrange(n)))
        edges.extend(skipper(n, random.randrange(n)))
    edges = [(v,w) for (v,w) in edges if v != w]
    edges = list(set(edges))
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
