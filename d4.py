from functools import lru_cache

lines = open('i4.txt').read().splitlines()
# lines = open('e4.txt').read().splitlines()
s = 0
cards = []
for l in lines:
    c,numbers = l.split(':')
    winning, mine = numbers.split('|')
    winning = [int(x) for x in winning.strip().split(' ') if x != '']
    mine = [int(x) for x in mine.strip().split(' ') if x != '']
    count = -1
    for n in mine:
        if n in winning:
            count += 1
    if count >= 0:
        s += pow(2, count)
    cards.append(count+2)
print(s)

@lru_cache(maxsize=None)
def get_number_of_copies(n):
    c = cards[n]
    s = 0
    for i in range(n+1,min(n+c, len(cards))):
        s += get_number_of_copies(i)
    return s + 1

s = 0
for i in range(len(cards)-1, -1, -1):
    a = get_number_of_copies(i)
    s += a
print(s)