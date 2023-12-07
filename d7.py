from collections import Counter

card_val = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9,
            '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3,
            '2': 2}

def fix_hand(hand):
    res = []
    for c in hand:
        res.append(card_val[c])
    return res

file_name = 'i7.txt'
# file_name = 'e7.txt'

hands = [(fix_hand(hand), int(bid)) for hand, bid in [line.split() for line in open(file_name).read().split('\n')]]

def generate_joker_values(n):
    if n == 0:
        yield []
    else:
        tail = list(generate_joker_values(n-1))
        for i in range(2,15):
            for t in tail:
                res = [i, *t]
                yield res

def hand_value(h, original=None):
    hand, _ = h
    if original is None:
        original = hand
    counted = Counter(hand).most_common()
    m = max([n for _,n in counted])
    l = len(counted)
    if m == 5:
        return [6, *original]
    elif m == 4:
        return [5, *original]
    elif l == 2:
        return [4, *original]
    elif m == 3:
        return [3, *original]
    elif l == 3:
        return [2, *original]
    elif m == 2:
        return [1, *original]
    else:
        return [0, *original]

def hand_value2(h):
    hand, _ = h
    hand = [c if c != 11 else 1 for c in hand]
    original = hand.copy()
    jokers = [i for i, x in enumerate(hand) if x == 1]
    joker_values = generate_joker_values(len(jokers))

    maxval = []
    for jv in joker_values:
        for j, v in zip(jokers, jv):
            hand[j] = v
        v = hand_value((hand, _), original)
        if v > maxval:
            maxval = v
    return maxval


s = 0

for rank, (hand, bid)  in enumerate(sorted(hands, key=hand_value), start=1):
    s += rank*bid

print(s)

s = 0

for rank, (hand, bid)  in enumerate(sorted(hands, key=hand_value2), start=1):
    s += rank*bid

print(s)