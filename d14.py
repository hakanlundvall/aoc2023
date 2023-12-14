data = open('i14.txt').read().splitlines()
block = list(map(''.join, zip(*data[0:])))
block = data[:]

def slide(block):
    new_block = []
    for line in block:
        a = line.split('#')
        b = [''.join(sorted(x, reverse=False)) for x in a] 
        c = '#'.join(b)
        new_block.append(c)
    return new_block

def load(block):
    s = 0
    for line in block:
        for i,x in enumerate(line):
            if x == 'O':
                s += 1 + i
    return s

def spin(block):
    return list(reversed(list(map(''.join, zip(*block)))))

def spin2(block):
    a = block[:]
    for i in range(3):
        a = spin(a[:])
    return a

def print_block(block):
    a = block[:]
    for l in a:
        print(l)
    print()

print(load(slide(spin2(block))))

from collections import defaultdict

c = defaultdict(int)
trace = []
for j in range(100000):
    for i in range(4):
        block = spin2(block[:])
        block = slide(block[:])

    v = load(spin2(block))
    c[v] += 1
    trace.append(v) 
    
    if max(c.values()) > 25:
        break

d = [y for x,y in c.items() if y > 5]

period = len(d)
start = j-period
print(trace[start+(1000000000-1-start)%period])


