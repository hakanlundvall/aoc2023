data = """Time:        61     70     90     66
Distance:   643   1184   1362   1041"""

# data = """Time:      7  15   30
# Distance:  9  40  200"""


time, dist = [x.split(':')[1].strip() for x in data.splitlines()]
time = [int(x) for x in time.split()]
dist = [int(x) for x in dist.split()]

time2, dist2 = [x.split(':')[1].strip() for x in data.splitlines()]
time2 = [int(''.join(time2.split()))]
dist2 = [int(''.join(dist2.split()))]

def get_dist(hold_time, total_time):
    run_time = total_time - hold_time
    dist = hold_time * run_time
    return dist

def calc(time,dist):
    res = 1
    for t, d in zip(time, dist):
        c = 0
        for i in range(1, t):
            if get_dist(i, t) > d:
                c = t-2*(i-1)-1
                break 
        res *= c
    return res

print(calc(time, dist))
print(calc(time2, dist2))