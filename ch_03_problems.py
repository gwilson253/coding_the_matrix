# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 14:59:27 2020

@author: greg.wilson
"""

from vec import Vec

# 3.1.3
def lin_comb(vlist, clist):
    return sum([v*c for v, c in zip(vlist, clist)])

from GF2 import one

# quiz 3.2.13 (wrong)
#def standard(D, one):
#    return [[one if j==i else 0 for j in range(len(D))] for i in range(len(D))]

# quiz 3.2.13 (right, but I get an assertion error)
def standard(D, one):
    return [Vec(D, {k: one}) for k in D]    

standard(['a'], one)