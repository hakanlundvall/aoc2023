lines = open("i3.txt").read().splitlines()
m = dict()

numbers = list()
gears = list()

for i, l in enumerate(lines):
    n = ""
    nc = list()
    for j, c in enumerate(list(l)):
        if c == "*":
            gears.append((i,j))
        m[(i,j)] = c
        if c.isdigit():
            n += c
            nc.append((i,j))
        elif n != "":
            numbers.append((n, nc))
            n = ""
            nc = list()
    if n != "":
        numbers.append((n, nc))


def neighbors(k):
    x, y = k
    yield (x-1, y-1)
    yield (x-1, y)
    yield (x-1, y+1)
    yield (x, y-1)
    yield (x, y+1)
    yield (x+1, y-1)
    yield (x+1, y)
    yield (x+1, y+1)

sum = 0

for k,v in numbers:
    number_found = False
    for n in v:
        for nn in neighbors(n):
            if nn in m and m[nn] not in ".0123456789":
                sum += int(k)
                number_found = True
                break
        if number_found:
            break

print(sum)
sum = 0
for g in gears:
    gs = list()
    for k, n in numbers:
        for gn in neighbors(g):
            if gn in n:
                gs.append(k)
                break
    if len(gs) == 2:
        sum += int(gs[0]) * int(gs[1])

print(sum)