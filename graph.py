import itertools
import sys


def add_edge(g, v, w, c):
    g[v].append((w,c))
    g[w].append((v,c))

def verify(g, vec):
    for v in range(len(g)):
        for w,c in g[v]:
            if c == red and vec[v] == vec[w]:
                return False
            if c == green and vec[v] != vec[w]:
                return False
    return True

green, red = 0, 1
if __name__ == "__main__":
        g = [list() for _ in range(18)]
        for r in [0, 6, 12]:
            # short red edges
            for i in range(r, r+6, 2):
                add_edge(g, i, i+1, red)
            # short green edges
            for i in range(r, r+4):
                add_edge(g, i, i+2, green)
            # second-shortest red edges
            add_edge(g, r, r+5, red)
            add_edge(g, r+1, r+4, red)
        # longest red edges
        for i in range(6):
            add_edge(g, i, i+6, green)
            add_edge(g, i+6, i+12, green)
            add_edge(g, i, 17-i, red)

        for vec in itertools.product([0,1], repeat=18):
            # print(vec)
            if verify(g, vec):
                print("Success: {}", vec)
        print("Done!")
