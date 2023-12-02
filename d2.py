#only 12 red cubes, 13 green cubes, and 14 blue cubes
limit = { 'red': 12, 'green': 13, 'blue': 14 }
lines = open('i2.txt').read().splitlines()
sum = 0
for l in lines:
    g, p = l.split(': ')
    r, c = g.split(' ')
    r = [x.split(', ') for x in p.split(';')]
    valid = True
    for a in r:
        for s in a:
            count, color = s.strip().split(' ')
            if int(count) > limit[color]:
                valid = False
                break
        if not valid:
            break
    if valid:
        sum += int(c)

print(sum)


limit = { 'red': 0, 'green': 0, 'blue': 0 }
lines = open('i2.txt').read().splitlines()
sum = 0
for l in lines:
    limit = { 'red': 0, 'green': 0, 'blue': 0 }
    g, p = l.split(': ')
    r, c = g.split(' ')
    r = [x.split(', ') for x in p.split(';')]
    for a in r:
        for s in a:
            count, color = s.strip().split(' ')
            if int(count) > limit[color]:
                limit[color] = int(count)
    p = limit['red'] * limit['green'] * limit['blue']
    sum += p
print(sum)