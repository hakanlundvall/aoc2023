lines1 = open('i12.txt').read().splitlines()

cache = dict()
def calc(a, b, pos, group_pos, current_group):
    key = (pos, group_pos, current_group)
    if key in cache:
        return cache[key]
    if pos==len(a):
        if group_pos==len(b) and current_group==0:
            return 1
        elif group_pos==len(b)-1 and b[group_pos]==current_group:
            return 1
        else:
            return 0
    ans = 0
    if a[pos] in ['.', '?']:
        if current_group==0:
            ans += calc(a, b, pos+1, group_pos, 0)
        elif current_group>0 and group_pos<len(b) and b[group_pos]==current_group:
            ans += calc(a, b, pos+1, group_pos+1, 0)
    if a[pos] in ['#', '?']:
      ans += calc(a, b, pos+1, group_pos, current_group+1)
    cache[key] = ans
    return ans


for p in [1,5]:

    lines = []
    for line in lines1:
        a,b = line.split()
        aa = [a] * p
        bb = [b] * p
        lines.append('?'.join([x for x in aa]) + ' ' + ','.join([x for x in bb]))


    s = 0
    for l in lines:
        a,b = l.split()
        r = a
        groups = [int(x) for x in b.split(',')] 
        cache = dict()
        s2 = calc(a, groups,0, 0, 0)
        # print(a, b, s2)
        s += s2
        
    print(s)
