import itertools
import sys
import matplotlib.pyplot as plt
from math import pi, sin, cos

green, red = 0, 1
cmap = ["green", "red"]

def show_graph(g):
    n = len(g)
    points = [ (cos(2*pi*v/n), sin(2*pi*v/n)) for v in range(n) ]
    rotations = [360*v/n-90 for v in range(n) ]

    for v in range(n):
        for w,c in g[v]:
            plt.plot([points[v][0], points[w][0]], [points[v][1], points[w][1]],
                     color=cmap[c], lw=2)

    for v in range(n):
        plt.plot(points[v][0], points[v][1], color="black", marker="o", markersize=10)
        plt.text(points[v][0]*1.1, points[v][1]*1.1, str(v),
                 horizontalalignment="center", verticalalignment="center", rotation=rotations[v], fontsize=10)


    plt.axis('off')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.gcf().canvas.set_window_title('Candidate Graph')
    plt.show()


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

if __name__ == "__main__":
        n = 18
        g = [list() for _ in range(n)]
        for r in [0, 6, 12]:
            # short red edges  (not needed for unique solution)
            # for i in range(r, r+6, 2):
            #     add_edge(g, i, i+1, red)
            for i in range(n):
                add_edge(g, i, (i+1)%n, red)
            # short green edges
            for i in range(r, r+4):
                add_edge(g, i, i+2, green)
            # second-shortest red edges
            add_edge(g, r, r+5, red)
            add_edge(g, r+1, r+4, red)
        # longest edges
        for i in range(6):
            add_edge(g, i, i+6, green)
            add_edge(g, i+6, i+12, green)
            add_edge(g, i, n-i-1, red)

        add_edge(g, 0, 7, green)  # TODO: remove, just a check

        for vec in itertools.product([0,1], repeat=18):
            # print(vec)
            if verify(g, vec):
                soln = ", ".join(["{}:{}".format(i, vec[i]) for i in range(n)])
                print("Success: {}".format(soln))
        print("Done!")

        show_graph(g)
