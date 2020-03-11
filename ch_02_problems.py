# -*- coding: utf-8 -*-
"""
Chapter 2 - The Vector 
Programming problems
Coding the Matrix
"""

from plotting import plot

L = [[2, 2], [3, 2], [1.75, 1], [2, 1], [2.25, 1], [2.5, 1], [2.75, 1], [3, 1], [3.25, 1]]

plot(L)

def add2(v, w):
    return [v[0]+w[0], v[1]+w[1]]

w = [1, 2]

plot([add2(_, w) for _ in L], 5)

# quiz 2.5.3
def scalar_vector_mult(alpha, v):
    return [alpha*v[i] for i in range(len(v))]

# task 2.5.4
alpha = -0.5
plot([[_[0]*alpha, _[1]*alpha] for _ in L])

plot([add2(scalar_vector_mult(i/100., [3, 2]), [0.5, 1]) for i in range(101)], 4)

# 2.6.9
def segment(pt1, pt2):
    return [add2(scalar_vector_mult(i/100., pt1),
                 scalar_vector_mult(1-i/100., pt2)) for i in range(101)]
    
plot(segment([3.5, 3], [0.5, 1.0]))

class Vec:
    def __init__(self, labels, function):
        self.D = labels
        self.f = function

v0 = Vec({'A', 'B', 'C'}, {'A': 1})  
      
# quiz 2.7.1
def zero_vec(D):
    f = {_: 0 for _ in D}
    return Vec(D, f)

v1 = zero_vec({'a', 'b', 'c'})

def setitem(v, d, val):
    v.f[d] = val

setitem(v0, 'B', 2)

def getitem(v, d):
    if d in v.f:
        return v.f[d]
    else:
        return 0
    
def scalar_mult(v, alpha):
    return Vec(v.D, {a: alpha*b for a, b in v.f.items()})

scalar_mult(v0, 2).f

def add(u, v):
    return Vec(u.D | v.D, {d: getitem(u, d) + getitem(v, d) for d in u.D | v.D})

v = Vec({'A', 'B', 'C'}, {'A': 1, 'B': 2})
u = Vec(v.D, {'A': 5, 'C': 10})

add(u, v).f

# quiz 2.7.5
def neg(v):
    return Vec(v.D, {d: getitem(v, d) * -1 for d in v.D})


# quiz 2.9.4
def list_dot(u, v):
    return sum([a*b for a, b in zip(u, v)])

# example 2.9.7
D = {'memory', 'radio', 'sensor', 'cpu'}
rate = Vec(D, {'memory': 0.06, 'radio': 0.1, 'sensor': 0.004, 'cpu': 0.0025})
duration = Vec(D, {'memory': 1.0, 'radio': 0.2, 'sensor': 0.5, 'cpu': 1.0})
list_dot(rate.f.values(), duration.f.values())

# quiz 2.9.13
haystack = [1, -1, 1, 1, 1, -1, 1, 1, 1]
needle = [1., -1., 1, 1., -1., 1.]

def dot_product_list(needle, haystack):
    result = []
    for i in range(len(haystack)-len(needle)+1):
        result.append(list_dot(haystack[i:i+len(needle)], needle))
    return result
    
dot_product_list(needle, haystack)

# quiz 2.10.1
from vec import Vec

#def list2vec(L):
#    return Vec(set(range(len(L))), {i: L[i] for i in range(len(L))})

# 2.11.4
from vecutil import list2vec, zero_vec
def triangular_solve_n(rowlist, b):
    D = rowlist[0].D
    n = len(D)
    assert D == set(range(n))
    x = zero_vec(D)
    for i in reversed(range(n)):
        x[i] = (b[i] - rowlist[i] * x)/rowlist[i][i]
    return x
    
D = {'a', 'b', 'c'}
rowlist = [Vec(D, {'a': 2, 'b': 3, 'c': -4}),
           Vec(D, {'b': 1, 'c': 2}),
           Vec(D, {'c': 5})]
b = Vec(D, {'a': 10, 'b': 3, 'c': 15})
triangular_solve_n(rowlist, b)

# 2.12 lab
with open('voting_record_dump109.txt') as f:
    mylist = list(f)

# 2.12.1
def create_voting_dict(strlist):
    x = [_.split() for _ in strlist]
    return {_[0]: [int(a) for a in _[3:]] for _ in x}

voting_dict = create_voting_dict(mylist)

# 2.12.2
def policy_compare(sen_a, sen_b, voting_dict):
    a = voting_dict[sen_a]
    b = voting_dict[sen_b]
    return sum([a[i]*b[i] for i in range(len(a))])
    
policy_compare('Reid', 'Obama', voting_dict)

# 2.12.3
def most_similar(sen, voting_dict):
    max_sim = None
    max_sen = None
    for s in voting_dict:
        if s == sen:
            continue
        sim = policy_compare(sen, s, voting_dict)
        if not max_sim:
            max_sim = sim
            max_sen = [s]
        if sim > max_sim:
            max_sim = sim
            max_sen = [s]
        if sim == max_sim and s not in max_sen:
            max_sen.append(s)
    return (max_sen, max_sim)

most_similar('Chafee', voting_dict)

# 2.12.4
def least_similar(sen, voting_dict):
    min_sim = None
    min_sen = None
    for s in voting_dict:
        if s == sen:
            continue
        sim = policy_compare(sen, s, voting_dict)
        if not min_sim:
            min_sim = sim
            min_sen = [s]
        if sim < min_sim:
            min_sim = sim
            min_sen = [s]
        if sim == min_sim and s not in min_sen:
            min_sen.append(s)
    return (min_sen, min_sim)

least_similar('Santorum', voting_dict)

# 2.12.6
policy_compare('Wyden', 'Smith', voting_dict)

# 2.12.7
def find_average_similarity(sen, sen_set, voting_dict):
    rslt = []
    for s in sen_set:
        rslt.append(policy_compare(sen, s, voting_dict))
    return sum(rslt)/len(rslt)

mylist2 = [_.split() for _ in mylist]
dems = [_[0] for _ in mylist2 if _[1]=='D']
repubs = [_[0] for _ in mylist2 if _[1]=='R']

find_average_similarity('Wyden', dems, voting_dict)

for sen in voting_dict:
    max_sim = None
    max_sen = None
    sim = find_average_similarity(sen, dems, voting_dict)
    if not max_sim:
        max_sim = sim
        max_sen = sen
    if sim > max_sim:
        max_sim = sim
        max_sen = sen
print(max_sen, max_sim)

# 2.12.8
def find_average_record(sen_set, voting_dict):
    sum_votes = None
    for sen in sen_set:
        if not sum_votes:
            sum_votes = voting_dict[sen]
        votes = voting_dict[sen]
        sum_votes = [sum_votes[i] + votes[i] for i in range(len(votes))]
    return [_ / len(votes) for _ in sum_votes]

avg_dem_rec = find_average_record(dems, voting_dict)

def policy_compare(sen_a, sen_b, voting_dict):
    a = voting_dict[sen_a]
    b = voting_dict[sen_b]
    return sum([a[i]*b[i] for i in range(len(a))])

for sen in voting_dict:
    max_sim = None
    max_sen = None
    sim = sum([voting_dict[sen][i]*avg_dem_rec[i] for i in range(len(avg_dem_rec))])
    if not max_sim:
        max_sim = sim
        max_sen = sen
    if sim > max_sim:
        max_sim = sim
        max_sen = sen
print(max_sen, max_sim)
    
# 2.12.6
min_sim = None
min_sens = None
for sen1 in voting_dict:
    for sen2 in voting_dict:
        if sen1 != sen2:
            sim = policy_compare(sen1, sen2, voting_dict)
            if not min_sim or sim < min_sim:
                min_sim = sim
                min_sens = (sen1, sen2)
print(min_sens, min_sim)