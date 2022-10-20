import graphlib
import math
import random
import sys
import itertools
import pprint


def CreateGraph (n,p):

    vertices = [i for i in range(n)]
    conexiones = [[0 for _ in range(n)] for _ in range(n)]
    # Show results
    for i in range(n):
        for j in range(n):
            if i != j:
                q = random.uniform(0, 1)
                if q < p:
                    v = random.randint(1, 100)
                    conexiones[i][j] = v
                    conexiones[j][i] = v
            # end if
        # end if
    # end for
# end for
    pprint.pprint(conexiones)
    return (vertices, conexiones)

def CoberturaBF (vertices, conexiones):
    topCover = vertices.copy()
    minCover = len(vertices)

    for r in range(1, len(vertices) + 1):
        for c in itertools.combinations(vertices, r):
            c = list(c)
            verCover = [False for _ in range(len(vertices))]

            for i in c:
                verCover[i] = True
                for j in range(len(vertices)):
                    if i != j and conexiones[i][j] > 0:
                        verCover[j] = True

            verTotCover = True
            i = 0
            while i < len(vertices) and verTotCover:
                if not verCover[i]:
                    verTotCover = False
                i += 1

            if verTotCover and len(c) < minCover:
                topCover = c
                minCover = len(c)


    print ("CoberturaBF: ", topCover)
    return 0

# -------------------------------------------------------------------------
# Read data
if len(sys.argv) < 3:
    print("Usage: python3", sys.argv[0], "n p")
    sys.exit(1)
# end if
n = int(sys.argv[1])
p = float(sys.argv[2])

vertices, conexiones = CreateGraph(n,p)
CoberturaBF(vertices, conexiones)