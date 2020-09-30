#!/bin/python3
g = [int(input()) for p in range(int(input()))]
[print(g1+5 - g1%5 if g1 > 37  and g1%5 > 2 else g1) for g1 in g]


