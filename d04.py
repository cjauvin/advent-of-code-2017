from collections import Counter

n_valid = 0
n_valid2 = 0
for i, l in enumerate(open('d4.txt')):
    ws = l.strip().split()
    n_valid += 1 if len(set(ws)) == len(ws) else 0
    n_valid2 += 1 if max(Counter(map(str, map(Counter, (map(sorted, ws))))).values()) == 1 else 0

print(n_valid)
print(n_valid2)

