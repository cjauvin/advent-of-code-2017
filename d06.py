import re
import numpy as np

a = "5	1	10	0	1	7	13	14	3	12	8	10	7	12	0	6"
#a = "0, 2, 7, 0"
a = map(int, re.split('\W+', a))
a = np.asarray(list(a))

def f(a):
    seen = set()
    n = 0
    while True:
        ta = tuple(a)
        if ta in seen:
            break
        seen.add(ta)
        i = np.argmax(a)
        q = a[i]
        a[i] -= q
        while q > 0:
            i += 1
            i %= len(a)
            a[i] += 1
            q -= 1
        n += 1
    return a, n

b, n = f(a)
print(b, n)
b, n = f(b)
print(b, n)
