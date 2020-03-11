# -*- coding: utf-8 -*-

# 0.8 problems

# 0.8.1
def increments(L): return [i + 1 for i in L]

increments([1, 5, 7]) == [2, 6, 8]

# 0.8.2
def cubes(L): return [i**3 for i in L]

cubes([1, 2, 3]) == [1, 8, 27]

# 0.8.3
def tuple_sum(A, B): return [(a[0]+b[0], a[1]+b[1]) for a, b in zip(A, B)]

tuple_sum([(1, 2), (10, 20)], [(3, 4), (30, 40)]) == [(4, 6), (40, 60)]

# 0.8.4
def inv_dict(d): return {v: k for k, v in d.items()}

inv_dict({'thank you': 'merci', 'goodbye': 'au revoir'})

# 0.8.5
def row(p, n): return [i + p for i in range(n)]

row(10, 4) == [10, 11, 12, 13]