#!/usr/bin/python3

import random
import sys

def graph(n, d):
    edges = [(i, (i+1)%(2*n)) for i in range(2*n)]
    for _ in range(d):
        perm = list(range(1, 2*n, 2))
        random.shuffle(perm)
        edges.extend([(2*i, perm[i]) for i in range(n)])
    return edges

def dot_output(edges, filename=None):
    of = sys.stdout
    if filename:
        of = open(filename, "w")
    of.write("graph{\n")
    for v,w in edges:
        of.write(" {} -- {};\n".format(v, w))
    of.write("}\n")


if __name__ == "__main__":
    n = 23
    d = 4
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    if len(sys.argv) > 2:
        d = int(sys.argv[2])
    dot_output(graph(n, d))
