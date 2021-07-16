#!/usr/bin/sage
""" Some code for computing the eigenvalue gap and related expansion
    parameters for d-regular graphs """

import random
import math
import sys

def alon_roichman(n, d):
  edges = list()
  for r in random.sample(range(1, (n-1)//2), d):
    edges.extend([(i, (i+r)%n) for i in range(n)])
  return sorted(set(edges))

def cycle(n):
  return [(i, (i+1) % n) for i in range(n)]

def adjacency_matrix(g):
  n = 1 + max(max(a,b) for (a,b) in g)
  m = [[0] * n for _ in range(n)]
  for (v,w) in g:
    m[v][w] = 1
    m[w][v] = 1
  return m

def print_matrix(m):
  for row in m:
    print(" ".join(str(x) for x in row))

log2ceil = lambda x : math.ceil(math.log(x, 2))

if __name__ == "__main__":
  n = 10
  if len(sys.argv) == 2:
    n = int(sys.argv[1])
  g = alon_roichman(n, min(n//2, 3*log2ceil(n)))
  #g = cycle(n)
  print("vertices = {}, edges = {}".format(n, len(g)))


  m = adjacency_matrix(g)
  #print_matrix(m)
  degrees = sorted(set([sum(row) for row in m]), reverse=True)
  print("degree(s):", " ".join(str(d) for d in degrees))

  eigenvalues = sorted((x.n() for x in matrix(m).eigenvalues()), reverse=True)

  lambda0 = eigenvalues[0]
  lambda1 = eigenvalues[1]
  gap = 1 - lambda1/lambda0
  print("eigenvalue gap = ", 1-lambda1/lambda0)

  d = degrees[0]
  h = d * gap / 2
  print("edge expansion is at least ", h)

  hout = 1 + h / d
  print("vertex expansion is at least ", hout)
  lambdax = max(-eigenvalues[0], lambda1)
  print("Mixing lemma lambda = ", lambdax)
