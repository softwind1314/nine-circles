#!/usr/bin/env python3

import itertools

per = itertools.permutations( [1,2,3], 2)

print(per)

print(type(per))

for p in per:
    print(p)
