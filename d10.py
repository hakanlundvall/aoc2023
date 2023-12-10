t = {'F': '┌', '-': '─', '7': '┐',
    '|': '│', 'L': '└', 'J': '┘'}
def tr(c):
    return t.get(c,c)

lines = open('i10.txt').read().splitlines()
map = {}
start = None
for r, l in enumerate(lines):
    for c, x in enumerate(l):
        map[(r,c)] = x
        if x == 'S':
            start = (r,c)

def get_neighbors(p, m):
    r,c = p
    for n in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
        if n in m:
            yield n

def connects(p1,p2,m):
    r1,c1 = p1
    r2,c2 = p2
    if r1 == r2:
        if c1 < c2:
            return m[p1] in '-LFS' and m[p2] in '-J7'
        else:
            return m[p1] in '-J7S' and m[p2] in '-LFS'
    elif c1 == c2:
        if r1 < r2:
            return m[p1] in '|F7S' and m[p2] in '|LJ'
        else:
            return m[p1] in '|LJS' and m[p2] in '|F7'
    else:
        return False

start_neigbors = []
for p in get_neighbors(start,map):
    if (connects(start,p,map)):
        start_neigbors.append(p)

d1 = start[0] - start_neigbors[0][0]
d2 = start[1] - start_neigbors[0][1]
d3 = start[0] - start_neigbors[1][0]
d4 = start[1] - start_neigbors[1][1]

if d1 == 0:
    if d2 < 0:
        start_dir1 = 'E'
    else:
        start_dir1 = 'W'
else:
    if d1 < 0:
        start_dir1 = 'S'
    else:
        start_dir1 = 'N'

if d3 == 0:
    if d4 < 0:
        start_dir2 = 'E'
    else:
        start_dir2 = 'W'
else:
    if d3 < 0:
        start_dir2 = 'S'
    else:
        start_dir2 = 'N'

dirs = ''.join(sorted([start_dir1,start_dir2]))

if dirs =='ES':
    map[start] = 'F'
elif dirs == 'NS':
    map[start] = '|'
elif dirs == 'NW':
    map[start] = 'J'
elif dirs == 'EW':
    map[start] = '-'
elif dirs == 'SW':
    map[start] = '7'
elif dirs == 'EN':
    map[start] = 'L'

def get_next(p,m, visited):
    for n in get_neighbors(p,m):
        if connects(p,n,m) and n not in visited:
            visited.add(n)
            yield n

visited = set()
visited.add(start)
n1 = list(get_next(start,map,visited))
p1, p2 = n1[0:1], n1[1:]

while True:
    n1 = list(get_next(p1[-1],map,visited))
    if n1:
        p1 +=  n1
    n2 = list(get_next(p2[-1],map,visited))
    if n2:
        p2 += n2
    if not n1 and not n2:   
        break

part1 = max([len(p1), len(p2)])

loop = set(p1+p2)
maxrow = len(lines)
maxcol = len(lines[0])

count = 0
for r in range(1,maxrow-1):
    c = 0
    hit_count = 0
    print()
    while c <= maxcol:
        if (r,c) not in loop:
            if hit_count%2 == 1:
                count += 1
                print('*', end='')
            else:
                print(' ', end='')
            c+=1
        else:
            print(tr(map[(r,c)]), end='')
            if map[(r,c)] == '|':
                hit_count+=1
                c+=1
            elif map[(r,c)] == 'L':
                enter_ = 'L'
                c+=1
                while c < maxcol and map[(r,c)] == '-':
                    print(tr(map[(r,c)]), end='')
                    c+=1
                exit_ = map[(r,c)]
                if exit_ == '7':
                    hit_count += 1
                else:
                    assert exit_ == 'J'
                print(tr(map[(r,c)]), end='')
                c+=1
            elif map[(r,c)] == 'F':
                enter_ = 'F'
                enter_c = c
                c+=1
                while c < maxcol and map[(r,c)] == '-':
                    print(tr(map[(r,c)]), end='')
                    c+=1
                exit_ = map[(r,c)]
                if exit_ == 'J':
                    hit_count += 1
                else:
                    assert exit_ == '7'
                print(tr(map[(r,c)]), end='')
                c+=1

print()
print(part1, count)