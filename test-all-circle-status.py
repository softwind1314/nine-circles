#!/usr/bin/env python3

def is_movable(g, i):
    ''' G for down-side, if true, it is in down-side'''
    if i == 1:
        return True
    if i == 2 and g[1] == False:
        return True

    if g[i-1] == False:
        if False not in g[1:i-1]:
            return True

    return False


#G = [False] * 10
#print(G)

#for i in range(1,9):
#    print( "{}: {}".format( i, is_movable(G, i) ) )


import sys


#G = [False] * 10
#G[2] = True
#print(G[1:])
#for i in range(1,6):
#    print( "{}: {}".format( i, is_movable(G, i) ) )


#sys.exit(0)


import itertools

per = itertools.permutations( [1,2,3,4,5], 2)

for p in per:
    G = [False] * 10
    for i in p:
        G[i] = True
    print(G[1:])
    for i in range(1,6):
        print( "{}: {}".format( i, is_movable(G, i) ) )

