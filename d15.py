data = open('i15.txt').read().split(',')
# data = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7".split(',')

def update_hash(data, hash):
    a = ord(data)
    hash += a
    hash *= 17
    hash %= 256
    return hash

def calc_hash(data):
    hash = 0
    for c in data:
        hash = update_hash(c, hash)
    return hash

s = 0
for d in data:
    hash = calc_hash(d)
    s += hash
    # print(hash)
        
print(s)
        
box = [[]] * 256    
for d in data:
    label = ""
    operator = ""
    for i, c in enumerate(d):
        if c in "-=":
            break
        label += c
    operator = d[i:]
    slot = calc_hash(label)

    if operator == '-':
        box[slot] = [(x, y) for x,y in box[slot] if x != label]
    elif operator[0] == '=':
        fl = int(operator[1:])
        old_box = box[slot][:]
        box[slot] = []
        added = False
        for i in old_box:
            if i[0] == label:
                box[slot].append((label, fl))
                added = True
            else:
                box[slot].append(i)
        if not added:
            box[slot].append((label, fl))
    else:
        assert False    

power_sum = 0
for bi, b in enumerate(box, 1):
    for li, (label, fl)  in enumerate(b, 1):
        power = bi*li*fl
        power_sum += power
print(power_sum)