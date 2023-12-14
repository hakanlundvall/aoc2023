data = open('i14.txt').read().splitlines()
block = list(map(''.join, zip(*data[0:])))

s=0
for line in block:
    print(line)
    a = line.split('#')
    b = [''.join(sorted(x, reverse=True)) for x in a] 
    c = '#'.join(b)
    for i,x in enumerate(c):
        if x == 'O':
            s += len(line) - i
print(s)