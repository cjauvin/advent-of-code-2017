import re
import functools
import numpy as np

N = 256
s = '83,0,193,1,254,237,187,40,88,27,2,255,149,29,42,100'

def part1(N, ls):
    a = list(range(N))
    p = 0
    skip = 0
    for l in ls:
        q = p + l
        q %= len(a)
        if q < p:
            # shift left for easier reverse
            a = np.roll(a, -p)
            a[:l] = a[:l][::-1]
            a = np.roll(a, p)
        else:
            a[p:q] = a[p:q][::-1]
        p += l + skip
        skip += 1
    return a[0] * a[1]

print(part1(N, map(int, re.split('\W+', s))))

assert functools.reduce(lambda x, y: x ^ y, map(int, re.split('\W+', '65 ^ 27 ^ 9 ^ 1 ^ 4 ^ 3 ^ 40 ^ 50 ^ 91 ^ 7 ^ 6 ^ 0 ^ 2 ^ 5 ^ 68 ^ 22'))) == 64

def reduce(a):
    assert len(a) == 256
    xor = functools.partial(functools.reduce, lambda x, y: x ^ y)
    return list(map(xor, np.split(a, 16)))

def part2(N, s):
    a = list(range(N))
    ls = list(map(ord, s)) + [17, 31, 73, 47, 23]
    p = 0
    skip = 0
    for i in range(64):
        for l in ls:
            q = p + l
            q %= len(a)
            if q < p:
                # shift left for easier reverse
                a = np.roll(a, -p)
                a[:l] = a[:l][::-1]
                a = np.roll(a, p)
            else:
                a[p:q] = a[p:q][::-1]
            p += l + skip
            skip += 1
    d = reduce(a)
    return ''.join(['{:02x}'.format(dd) for dd in d])

assert part2(N, '') == 'a2582a3a0e66e6e86e3812dcb672a272'
assert part2(N, 'AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd'
assert part2(N, '1,2,3') == '3efbe78a8d82f29979031a4aa0b16a9d'
assert part2(N, '1,2,4') == '63960835bcdc130f0b66d7ff4f6a5a8e'

print(part2(N, s))
