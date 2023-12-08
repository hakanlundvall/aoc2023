path, map = open('i8.txt').read().split('\n\n')
# path, map = open('e8.txt').read().split('\n\n')

m = {}
maplines = [x.split(' = ') for x in map.splitlines()]
for l, r in maplines:
    m[l] = tuple([x.strip('() ') for x in r.split(',')])

node = 'AAA'
steps = 0
done = False
while not done:
    for d in path:
        if d == 'L':
            node = m[node][0]
        elif d == 'R':
            node = m[node][1]
        else:
            assert False
        steps += 1
        if node == 'ZZZ':
            print(steps)
            done = True
            break

# path, map = open('e8.txt').read().split('\n\n')
m = {}
maplines = [x.split(' = ') for x in map.splitlines()]
for l, r in maplines:
    m[l] = tuple([x.strip('() ') for x in r.split(',')])

nodes = [x for x in  m.keys() if x.endswith('A')]
steps = 0
res = []
for n in nodes:
    done = False
    last_steps = 0
    diff = 0
    steps = 0
    while not done:
        for d in path:
            if d == 'L':
                n = m[n][0]
            elif d == 'R':
                n = m[n][1]
            else:
                assert False
            steps += 1
            if n.endswith('Z'):
                if (steps-last_steps) == diff:
                    res.append((steps, diff))
                    # print(steps, diff)
                    done = True
                    break
                diff = steps-last_steps
                last_steps = steps

from sympy.ntheory.modular import solve_congruence

print(solve_congruence(*res))