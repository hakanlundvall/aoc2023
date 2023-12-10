lines = open('i9.txt').read().splitlines()
# lines = open('e9.txt').read().splitlines()

def get_next(l):
    if all(x==0 for x in l):
        return 0
    else:
        n = []
        for i in range(1,len(l)):
            n.append(l[i]-l[i-1])
        return get_next(n) + l[-1]
    
def get_prev(l):
    if all(x==0 for x in l):
        return 0
    else:
        n = []
        for i in range(1,len(l)):
            n.append(l[i]-l[i-1])
        return l[0] - get_prev(n)
    


p = []
r = []
for line in lines:
    l = [int(x) for x in line.split()]
    p.append(get_next(l))
    r.append(get_prev(l))
print(sum(p), sum(r))