import itertools

lines = open('i11.txt').read().splitlines()

map = []
cols = set()
rows = set()
for r, l in enumerate(lines):
    for c, x in enumerate(l):
        if x == '#':
            map.append((r,c))
            cols.add(c)
            rows.add(r)


max_c = max(cols)
max_r = max(rows)
min_c = min(cols)
min_r = min(rows)
extra_row = []
extra_col = []

for c in range(min_c, max_c):
    if c not in cols:
        extra_col.append(c)
for r in range(min_r, max_r):
    if r not in rows:
        extra_row.append(r)


def dist(p1,p2, exp = 2):
    r1,c1 = p1
    r2,c2 = p2
    res = abs(r1-r2) + abs(c1-c2)
    for r in extra_row:
        if r1 < r < r2 or r2 < r < r1:
            res += exp-1
    for c in extra_col: 
        if c1 < c < c2 or c2 < c < c1:
            res += exp-1
    return res

pairs = list(itertools.combinations(map, 2))
dists = [dist(p1,p2) for p1,p2 in pairs]
print(sum(dists))
dists = [dist(p1,p2, exp=1000000) for p1,p2 in pairs]
print(sum(dists))

