#!/bin/python

import sys        

k = int(input().strip())
for a0 in xrange(t):
    n,c,m = input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]
    choc= n/c
    wrapper = chocs
    ex_choc = wrapper/m
    while wrapper >= m:
        ex_choc = wrapper / m
        wrapper = ex_choc + wrapper % m
        choc += ex_choc
    print(choc)

