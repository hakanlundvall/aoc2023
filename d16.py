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

m[(0,-1)] = ('.', [])
beams = [((0,-1), 0)]

def follow_beam(b):
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
        follow_beam((next_pos, dir))
    elif tile == '|':
        if dir in [0, 2]:
            dl = (dir+3)%4
            d2 = (dir+1)%4
            for dn in [dl, d2]:
                follow_beam((next_pos, dn))
        else:
            follow_beam((next_pos, dir))        
    elif tile == '-':
        if dir in [1, 3]:
            dl = (dir+3)%4
            d2 = (dir+1)%4
            for dn in [dl, d2]:
                follow_beam((next_pos, dn))
        else:
            follow_beam((next_pos, dir))        
    elif tile == '/':
        if dir in [0, 2]:
            follow_beam((next_pos, (dir+3)%4))
        else:
            follow_beam((next_pos, (dir+1)%4))

    elif tile == '\\':
        if dir in [0, 2]:
            follow_beam((next_pos, (dir+1)%4))
        else:
            follow_beam((next_pos, (dir+3)%4))

for p in beams:
    follow_beam(p)

del m[(0,-1)]


print(sum([1 for pos, dirs in m.items() if len(dirs[1]) > 0]))
