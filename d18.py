lines = open('i18.txt').read().splitlines() 

m=dict()

dirs = {'R':(0,1), 'L':(0,-1), 'D':(1,0), 'U':(-1,0)}

pos = (0,0) 
for line in lines:
    d, l, c = line.split()
    for i in range(int(l)):
        pos = (pos[0]+dirs[d][0], pos[1]+dirs[d][1])
        m[pos] = c
        
rows = [r for (r,c) in m.keys()]
cols = [c for (r,c) in m.keys()]
min_row = min(rows)
max_row = max(rows)
min_col = min(cols)
max_col = max(cols)
   
def print_map(m):
    for r in range(min_row, max_row+1):
        for c in range(min_col, max_col+1):
            if (r,c) in m:
                print('X', end='')
            else:
                print('.', end='')
        print()
        
# print_map(m)

trench = m.copy()

for r in range(min_row, max_row+1):
    count = 0
    crossings = 0
    from_above = False
    from_below = False
    for c in range(min_col, max_col+1):
        if (r,c) in trench:
            if count == 0:
                count = 1
                if (r-1,c) in trench:
                    from_above = True
                if (r+1,c) in trench:   
                    from_below = True
            else:
                count += 1
        else:
            if count > 0:
                if from_above and from_below:
                    crossings += 1
                else:
                    if (r-1,c-1) in trench and from_below:
                        crossings += 1
                    if (r+1,c-1) in trench and from_above:
                        crossings += 1   
                    
                count = 0
                from_above = False
                from_below = False
            if crossings%2 == 1:                
                m[(r,c)] = 'X'

# print_map(m)

print(len(m.keys()))