import re

s = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""

def part1():

    T = {}

    #for l in s.split('\n'):
    for l in open('d7.txt'):
        m = re.match('(.*?) \(\d+\)(?: -> (.*))?', l).groups()
        name = m[0]
        if name not in T:
            T[name] = []
        children = []
        if m[1]:
            children = re.split('\W+', m[1])
            for c in children:
                if c not in T:
                    T[c] = None
                T[c] = name
        #print(name, children)

    for c, p in T.items():
        if not p:
            return c


T = {} # child -> parent
W = {} # n -> weight

#for l in s.split('\n'):
for l in open('d7.txt'):
    m = re.match('(.*?) \((\d+)\)(?: -> (.*))?', l).groups()
    name = m[0]
    if name not in T:
        T[name] = []
    W[name] = int(m[1])
    children = []
    if m[2]:
        children = re.split('\W+', m[2])
        for c in children:
            if c not in T:
                T[c] = None
            T[c] = name

#print(T)
#W['ugml'] -= 8
#W['ncrxh'] -= 5

def find_children(n=[]):
    return [c for c, p in T.items() if p == n]

def build_tree(n=[]):
    return {c: build_tree(c) for c in find_children(n)}

def visit(parent=[]):
    wl = []
    ws = set()
    for c in find_children(parent):
        w = visit(c)
        ws.add(w)
        wl.append((c, w))
    if len(ws) > 1:
        print(wl)
    return -1 if parent == [] else W[parent] + sum(a[1] for a in wl)
