def dist(N):
    k = 8
    low = 1
    hi = 2
    v = hi - 1
    d = -1
    n = 2
    if N <= 1:
        return 0
    elif N == 2:
        return 1
    while True:
        # k=8:  1 2 1 2 1 2 1 2                                   low=1, hi=2
        # k=16: 3 2 3 4 3 2 3 4 3 2 3 4 3 2 3 4                   low=2, hi=4
        # k=24: 5 4 3 4 5 6 5 4 3 4 5 6 5 4 3 4 5 6 5 4 3 4 5 6   low=3, hi=6
        # k=32: 7 6 5 4 5 6 7 8                                   low=4, hi=8
        # k=40: 9 8 7 6 5 6 7 8 9 10 9
        for _ in range(k):
            if v == hi:
                d = -1
            elif v == low:
                d = 1
            v += d
            if n == N - 1:
                return v
            n += 1
        k += 8
        low += 1
        hi += 2
        v = hi - 1


# assert dist(1) == 0
# assert dist(12) == 3
# assert dist(23) == 2
# assert dist(1024) == 31

# print(dist(361527))

def get_neighbor_sum(g, j, i):
    s = 0
    for ii in [-1, 0, 1]:
        for jj in [-1, 0, 1]:
            if ii == 0 and jj == 0: continue
            s += g[i+ii][j+jj]
    return s

# g_test = [[1,2,3],[4,5,6],[7,8,9]]
# print(get_neighbor_sum(g_test, 1, 1))

def part2(min_sum):

    N = 15
    g = [[0] * N for _ in range(N)]
    x = N // 2
    y = N // 2
    xy = [x, y]

    g[y][x] = 1

    d = 1

    while True:
        aa = [1, -1, -1, 1] # dir
        aaa = 0
        for dd in [d, d + 1]: # side length
            for z in (0, 1): # x/y
                for _ in range(dd): # do side
                    xy[z] += aa[aaa]
                    g[xy[1]][xy[0]] = get_neighbor_sum(g, xy[0], xy[1])
                    if g[xy[1]][xy[0]] > min_sum:
                        return g[xy[1]][xy[0]]
                aaa += 1
                aaa %= 4

        d += 2

def print_grid(g):
    for r in g:
        print(' '.join(['{:4d}'.format(i) for i in r]))

assert part2(800) == 806

print(part2(361527))
