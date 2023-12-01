

d = open("i1.txt", "r").read().splitlines()
s = 0
for l in d:
    l2 = [int(x) for x in l if x.isnumeric()]
    s += l2[0]*10 + l2[-1]

print(s)

m = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six":"6", "seven": "7", "eight": "8", "nine": "9"}

d = open("i1.txt", "r").read().splitlines()
s = 0
for l in d:
    l3= []
    a = ""
    for i in l:
        if i.isnumeric():
            l3.append(i)
            a = ""
        else:
            a += i
        for k in m.keys():
            if a.endswith(k):
                l3.append(m[k])
                a = ""
    l2 = [int(x) for x in l3 if x.isnumeric()]

    s += l2[0]*10 + l2[-1]

print(s)
