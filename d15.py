def part1(a, b):
    n = 0
    for i in range(40000000):
        a = (a * 16807) % 2147483647
        b = (b * 48271) % 2147483647
        #print(a, b)
        n += 1 if bin(a)[-16:] == bin(b)[-16:] else 0
    return n

assert part1(65, 8921) == 588
assert part1(873, 583) == 631

def part2(a, b):

    def get_gen(val, mult, div):
        def gen():
            nonlocal val, mult, div
            while True:
                val = (val * mult) % 2147483647
                if val % div == 0:
                    yield val
        return gen()

    ga = get_gen(a, 16807, 4)
    gb = get_gen(b, 48271, 8)
    n = 0
    for i in range(5000000):
        a = next(ga)
        b = next(gb)
        n += 1 if bin(a)[-16:] == bin(b)[-16:] else 0
    return n

assert part2(65, 8921) == 309
assert part2(873, 583) == 279
