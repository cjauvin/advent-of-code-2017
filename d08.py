import re
import operator
from collections import defaultdict

s = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""

ops = {'<': operator.__lt__, '>': operator.__gt__, '<=': operator.__le__, '>=': operator.__ge__, '==': operator.__eq__, '!=': operator.__ne__}

R = defaultdict(int)

max_value = 0

#for l in s.split('\n'):
for l in open('d8.txt'):
    m = re.match('(.+) (inc|dec) ([0-9-]+) if (.+) (.+) ([0-9-]+)', l).groups()
    if ops[m[4]](R[m[3]], int(m[5])):
        v = int(m[2])
        R[m[0]] += v if m[1] == 'inc' else -v
        max_value = max(max_value, R[m[0]])

print(max(R.values()))
print(max_value)
