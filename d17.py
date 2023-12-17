from queue import PriorityQueue
data = open('i17.txt').read().splitlines()

m = dict()
for r, line in enumerate(data):
    for c, char in enumerate(line):
        m[(r,c)] = int(char)
max_r = len(data)
max_c = len(data[0])
        
def at_target(state):
    heat, steps, dir, pos = state
    r,c = pos
    if r==max_r-1 and c==max_c-1:
        return True
    return False

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

def next_states(state, part2 = False):
    heat, steps, dir, pos = state
    r,c = pos
    
    if steps < (10 if part2 else 3):
        next_pos = take_step(pos, dir)
        if next_pos:
            yield (heat+m[next_pos], steps+1, dir, next_pos)
    if not part2 or (steps == 0 or steps >= 4):
        dir = (dir+1)%4
        next_pos  = take_step(pos, dir)
        if next_pos:
            yield (heat+m[next_pos], 1, dir, next_pos)
        dir = (dir+2)%4
        next_pos  = take_step(pos, dir)
        if next_pos:
            yield (heat+m[next_pos], 1, dir, next_pos)

def bfs(state, part2 = False):
    queue = PriorityQueue()
    queue.put(state)
    visited = dict()
    while queue.not_empty:
        state = queue.get()
        heat, steps, dir, pos = state
        key = (steps, dir, pos)
        best = visited.get(key, 10**10)
        if heat < best:
            visited[key] = heat
        else:
            continue
        if at_target(state):
            return state
        for next_state in next_states(state, part2):
            queue.put(next_state)

for part2 in [False, True]:
    print(bfs((0, 0, 0, (0,0)), part2)[0])
