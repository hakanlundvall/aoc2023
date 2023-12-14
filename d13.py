from collections import Counter

data = open('i13.txt').read().split('\n\n')
# data = open('e13.txt').read().split('\n\n')

def fold(line, n):
    l = len(line)
    a = line[:n]
    b = ''.join(list(reversed(line[n:])))
    if n < l/2:
        b = b[-n:]
    if n > l/2:
        a = a[n-l:]
    
    return a == b

def calc(line):
    for n in range(1, len(line)):
        if fold(line, n):
            yield n
     
    
s = 0
for block in data:
    p = []
    bl = block.splitlines()
    for line in bl:   
        # print(line)
        for x in calc(line):
            p.append(x)
    c = Counter(p)
    c_keys = [key for key, count in c.items() if count == len(bl)]
    assert len(c_keys) in [0,1]
    # print(sum(c_keys))
    s += sum(c_keys)
    # print()
    
    p = []
    bl2 = list(map(''.join, zip(*bl[0:])))  # Transpose of bl
    for line in bl2:   
        # print(line)
        for x in calc(line):
            p.append(x)
    
    c = Counter(p)
    c_keys = [100 * key for key, count in c.items() if count == len(bl2)]
    assert len(c_keys) in [0,1]
    # print(sum(c_keys))
    s += sum(c_keys)
    # print()
print(s)


def mirror(block, n, depth, smudge):
    i1 = n-1-depth
    i2 = n+depth
    if i1 < 0 or i2 >= len(block):
        return smudge
    diff = [x==y for x,y in zip(block[i1], block[i2])]
    if Counter(diff)[False] == 1 and not smudge:
        return mirror(block, n, depth+1, True)
    elif Counter(diff)[False] == 0:
        return mirror(block, n, depth+1, smudge)
    else:
        return False

s = 0
for block in data:
    p = []
    bl = block.splitlines()
    for i in range(1, len(bl)):
        if mirror(bl, i, 0, False):
            p.append(i)
    s += sum(p) * 100
            
    p = []
    bl2 = list(map(''.join, zip(*bl[0:])))  # Transpose of bl

    for i in range(1, len(bl2)):
        if mirror(bl2, i, 0, False):
            p.append(i)
    s += sum(p)
    
print(s)
