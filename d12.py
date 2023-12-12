import itertools
lines = open('i12.txt').read().splitlines()

# lines = ['?###???????? 3,2,1']



def test(r, groups):
    t = [len(x) for x in ''.join(r).split('.') if len(x) > 0]
    return t == groups


s = 0
for l in lines:
    a,b = l.split()
    
    wildcards = [i for i,x in enumerate(a) if x == '?']
    wildcard_count = len(wildcards)
    springs = [i for i,x in enumerate(a) if x == '#']    
    counts = [int(x) for x in b.split(',')]
    spring_count = sum(counts)-len(springs)
    a = list(a)
    for t in itertools.combinations(range(wildcard_count), spring_count):
        for i in range(wildcard_count):
            if i in t:
                a[wildcards[i]] = '#'
            else:
                a[wildcards[i]] = '.'
        if test(a, counts):
            s += 1 

print(s)