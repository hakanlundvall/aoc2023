lines = open('i5.txt').read().split('\n\n')
# lines = open('e5.txt').read().split('\n\n')
seeds = [int(x) for x in lines[0].split(':')[1].strip().split(' ')]
# print(seeds)

def get_map(part):
    return [ [int(y) for y in x.strip().split()] for x in part.splitlines()[1:]]

maps = [get_map(x) for x in lines[1:]]

def solve(seeds):
    paths = []

    for s in seeds:
        n = [s]
        for i in range(len(maps)):
            m = maps[i]
            next = n[-1]
            for r in m:
                if r[1] <= n[-1] < r[1]+r[2]:
                    next = n[-1] - r[1] + r[0]
                    break
            n.append(next)
        paths.append(n)
    return sorted([x[-1] for x in paths])[0]
print(solve(seeds))

def solve2(seed_ranges):
    paths = []
    s = seed_ranges[:]

    def split_intervals(a, b):
        a_start, a_end = a[0], a[0]+a[1]
        b_start, b_end = b[1], b[1]+b[2]
        splits = [a_start, a_end]
        if a_start < b_start < a_end:
            splits = sorted(splits + [b_start])
        if a_start < b_end < a_end:
            splits = sorted(splits + [b_end])
        while len(splits) > 1:
            yield (splits[0], splits[1]-splits[0])
            splits = splits[1:]

    def get_next(ranges, map):
        ranges2 = ranges[:]
        for m in map:
            ranges1 = ranges2[:]
            ranges2 = []
            for r in ranges1:
                ranges2 += list(split_intervals(r, m))
        ranges3 = []
        for s,l in ranges2:
            for m in map:
                if s >= m[1] and s < m[1]+m[2]:
                    ranges3.append((s-m[1]+m[0], l))
                    break
            else:
                ranges3.append((s,l))
        return ranges3



    for m in maps:
        s = get_next(s, m)

    return sorted([x[0] for x in s])[0]

length1 = [1] * len(seeds)
print(solve2(list(zip(seeds, length1))))
start2 = seeds[::2]
length2 = seeds[1::2]
print(solve2(list(zip(start2, length2))))

