from collections import defaultdict
lines = open('i18.txt').read().splitlines() 
# lines = open('e18.txt').read().splitlines() 

m=dict()

dirs = {'R':(0,1), 'L':(0,-1), 'D':(1,0), 'U':(-1,0)}

vertical_lines = []

pos = (0,0) 
pos2 = (0,0)

for line in lines:
    d, l, c = line.split()
    for i in range(int(l)):
        pos = (pos[0]+dirs[d][0], pos[1]+dirs[d][1])
        m[pos] = c
    l2 = int(c[2:-2],16)
    d2 = int(c[-2])
    if d2 == 1: #Down
        next_pos = (pos2[0]+l2, pos2[1])
        vertical_lines.append((pos2, next_pos))
        pos2 = next_pos
    elif d2 == 3: #Up 
        next_pos = (pos2[0]-l2, pos2[1])
        vertical_lines.append((next_pos, pos2))
        pos2 = next_pos
    elif d2 == 2: #Left
        next_pos = (pos2[0], pos2[1]-l2)
        pos2 = next_pos
    elif d2 == 0: #Right
        next_pos = (pos2[0], pos2[1]+l2)
        pos2 = next_pos
    else:
        assert False
    
rows = [r for (r,c) in m.keys()]
cols = [c for (r,c) in m.keys()]
min_row = min(rows)
max_row = max(rows)
min_col = min(cols)
max_col = max(cols)
   

trench = m.copy()

for r in range(min_row, max_row+1):
    count = 0
    crossings = 0
    from_above = False
    from_below = False
    for c in range(min_col, max_col+1):
        if (r,c) in trench:
            if count == 0:
                count = 1
                if (r-1,c) in trench:
                    from_above = True
                if (r+1,c) in trench:   
                    from_below = True
            else:
                count += 1
        else:
            if count > 0:
                if from_above and from_below:
                    crossings += 1
                else:
                    if (r-1,c-1) in trench and from_below:
                        crossings += 1
                    if (r+1,c-1) in trench and from_above:
                        crossings += 1   
                    
                count = 0
                from_above = False
                from_below = False
            if crossings%2 == 1:                
                m[(r,c)] = 'X'

print(len(m.keys()))


def merge(l):
    merged = []
    for i in l:
        if len(merged) == 0:
            merged.append(i)
        else:
            if i[0] <= merged[-1][1]:
                merged[-1] = (merged[-1][0], max(merged[-1][1], i[1]))
            else:
                merged.append(i)
    return merged

def merge_stripes(current_stripes, new_stripes):
    it1 = iter(current_stripes)
    it2 = iter(new_stripes)
    s1 = []
    s2 = []
    for i in  it1:
        s1.append((i, next(it1)))
    for i in it2:
        s2.append((i, next(it2)))

    s3 = merge(sorted(s1+s2))
    s4 = []
    for a,b in s3:
        s4.append(a)
        s4.append(b)
    return s4

def stripe_lengths(current_stripes):
    it1 = iter(current_stripes)
    s1 = []
    for i in  it1:
        s1.append((i, next(it1)))
    s = 0
    for a,b in s1:
        s += (1+b-a)    
    return s

edge_vals = set()
for vl in vertical_lines:
    edge_vals.add(vl[0][0])
    edge_vals.add(vl[1][0])
    
edge_vals = sorted(list(edge_vals))

def find_crossings(vertical_lines, edge_val):
    crossings = []
    starting = []
    ending = []
    for vl in vertical_lines:
        r1, r2 = sorted([vl[0][0], vl[1][0] ])
        if r1 == edge_val:
            starting.append(vl)
        elif r2 == edge_val:    
            ending.append(vl)
        elif r1 <= edge_val and r2 >= edge_val:
            crossings.append(vl)
    return starting, ending, crossings

current_stripes = []
previous_edge = 0
edges_s = 0
blocks_s = 0

for e in edge_vals:
    it = iter(current_stripes)
    assert e > previous_edge or previous_edge == 0
    
    starting, ending, crossings = find_crossings(vertical_lines, e)
    new_stripes = [a for ((_,a),(_,_)) in starting]
    continuing_stripes = [a for ((_,a),(_,_)) in crossings]
    new_current_stripes = sorted(continuing_stripes + new_stripes)

    a = merge_stripes(current_stripes, new_current_stripes)
    sl = stripe_lengths(a)
    blocks_s += stripe_lengths(current_stripes) * (e-previous_edge-1)
    edges_s += sl 
    previous_edge = e
    current_stripes = new_current_stripes
    assert len(current_stripes)%2 == 0

print(edges_s+blocks_s)