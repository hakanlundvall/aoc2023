lines = open('i18.txt').read().splitlines() 
# lines = open('e18.txt').read().splitlines() 

dirs = {'R':(0,1), 'L':(0,-1), 'D':(1,0), 'U':(-1,0)}
dirs2 = {'0':(0,1), '2':(0,-1), '1':(1,0), '3':(-1,0)}

pos = (0,0) 
pos2 = (0,0)
coords = [pos]
coords2 = [pos2]

for line in lines:
    d, l, c = line.split()
    step = tuple([x*int(l) for x in dirs[d]])
    pos = (pos[0]+step[0], pos[1]+step[1])
    coords.append(pos)
    
    l2 = int(c[2:-2],16)
    d2 = c[-2]
    step = tuple([x*int(l2) for x in dirs2[d2]])
    pos2 = (pos2[0]+step[0], pos2[1]+step[1])
    coords2.append(pos2)
  
def shoelace_area(coord_list):
    n = len(coord_list)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += coord_list[i][0] * coord_list[j][1]
        area -= coord_list[j][0] * coord_list[i][1]
    area = abs(area) // 2
    return area    

def circumference(coord_list):
    c = 0
    for i in range(len(coord_list)-1):
        c += abs(coord_list[i][0]-coord_list[i+1][0]) + abs(coord_list[i][1]-coord_list[i+1][1])
    return c

print(shoelace_area(coords) + 1 + circumference(coords)//2)
print(shoelace_area(coords2) + 1 + circumference(coords2)//2)

