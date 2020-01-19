# -*- coding: utf-8 -*-

with open('stories_big.txt', 'r') as f:
    stories = f.readlines()
    
def makeInverseIndex(strlist):
    words = set(' '.join(strlist).split())
    story_index = {i: j for i, j in enumerate(strlist)}
    return {w: {k for k, v in story_index.items() if w in v.split()} for w in words}
    
inv_index = makeInverseIndex(stories)

def orSearch(inverseIndex, query):
    results = set()
    filtered = [v for k, v in inverseIndex.items() if k in query]
    for v in filtered:
        results.update(v)
    return results
    
def andSearch(inverseIndex, query):
    
    filtered = {k: v for k, v in inverseIndex.items() if k in query}
    
    if len(filtered.values()):
        results = list(filtered.values())[0]
    else:
        results = set()
        
    if len(filtered.values()) > 1:
        for v in list(filtered.values())[1:]:
            results = results & v
            
    return results

# note - andSearch doesn't work if one of the query terms isn't in the inverse index

a = inv_index['taco']
b = inv_index['fruit']