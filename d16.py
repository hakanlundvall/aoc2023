data = open('i16.txt').read().splitlines()
# data = open('e16.txt').read().splitlines()
import sys
sys.setrecursionlimit(1000000)
m = dict()
for r, line in enumerate(data):
    for c, char in enumerate(line):
        m[(r,c)] = (char, [])
max_r = len(data)
max_c = len(data[0])

start_dict = m.copy()
        
def take_step(pos, dir):
    r,c = pos
    if dir==0:
        c += 1
    elif dir==1:
        r += 1
    elif dir==2:
        c -= 1
    elif dir==3:
        r -= 1
    if r<0 or r>=max_r or c<0 or c>=max_c:
        return None
    return (r,c)


def follow_beam(b, m):
    pos, dir = b
    tile, dirs = m[pos]
    if dir in dirs:
        return
    else:
        m[pos] = (tile, dirs + [dir])
    next_pos = take_step(pos, dir)
    if not next_pos:
        return
    tile, dirs = m[next_pos]

    if tile == '.':
        follow_beam((next_pos, dir), m)
    elif tile == '|':
        if dir in [0, 2]:
            dl = (dir+3)%4
            d2 = (dir+1)%4
            for dn in [dl, d2]:
                follow_beam((next_pos, dn), m)
        else:
            follow_beam((next_pos, dir), m)        
    elif tile == '-':
        if dir in [1, 3]:
            dl = (dir+3)%4
            d2 = (dir+1)%4
            for dn in [dl, d2]:
                follow_beam((next_pos, dn), m)
        else:
            follow_beam((next_pos, dir), m)        
    elif tile == '/':
        if dir in [0, 2]:
            follow_beam((next_pos, (dir+3)%4), m)
        else:
            follow_beam((next_pos, (dir+1)%4), m)

    elif tile == '\\':
        if dir in [0, 2]:
            follow_beam((next_pos, (dir+1)%4), m)
        else:
            follow_beam((next_pos, (dir+3)%4), m)

def start(start_pos, start_dir):
    m = start_dict.copy()
    m[start_pos] = ('.', [])

    follow_beam((start_pos, start_dir), m)

    del m[start_pos]

    return sum([1 for pos, dirs in m.items() if len(dirs[1]) > 0])



print(start((0,-1), 0))
candidates = []
for r in range(max_r):
    candidates.append(start((r,-1), 0))
    candidates.append(start((r,max_c), 2))
for c in range(max_c):
    candidates.append(start((-1,c), 1))
    candidates.append(start((max_r,c), 3))

print(max(candidates))