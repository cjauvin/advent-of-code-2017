import numpy as np
import functools
from collections import Counter


def reduce(a):
    assert len(a) == 256
    xor = functools.partial(functools.reduce, lambda x, y: x ^ y)
    return list(map(xor, np.split(a, 16)))

def knot_hash(N, s):
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
    return ''.join([f'{i:02x}' for i in d])

N = 256

# assert part2(N, '') == 'a2582a3a0e66e6e86e3812dcb672a272'
# assert part2(N, 'AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd'
# assert part2(N, '1,2,3') == '3efbe78a8d82f29979031a4aa0b16a9d'
# assert part2(N, '1,2,4') == '63960835bcdc130f0b66d7ff4f6a5a8e'

def to_binary(hx):
    return ''.join(['{0:04b}'.format(int(h, 16)) for h in hx])

assert to_binary('a0c2017') == '1010000011000010000000010111'

def part1(code):
    n_squares = 0
    for i in range(128):
        h = knot_hash(N, f'{code}-{i}')
        b = to_binary(h)
        n_squares += Counter(b)['1']
    return n_squares

def part2(code):
    g = [to_binary(knot_hash(N, f'{code}-{i}')) for i in range(128)]
    visited = set()

    def do_cluster(i, j):
        visited.add((i, j))
        to_try = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        while to_try:
            i, j = to_try.pop()
            if (i, j) in visited:
                continue
            if not (0 <= i < 128 and 0 <= j < 128):
                continue
            visited.add((i, j))
            if g[i][j] == '1':
                to_try += [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]

    n = 0
    for i in range(128):
        for j in range(128):
            if (i, j) in visited or g[i][j] == '0':
                continue
            do_cluster(i, j)
            n += 1
    return n

assert part2('flqrgnkx') == 1242
assert part2('hxtvlmkl') == 1093
