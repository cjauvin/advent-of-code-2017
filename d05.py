#ins = [0, 3, 0, 1, -3]

ins = []
for l in open('d5.txt'):
    ins.append(int(l.strip()))
assert ins[0] == 0
assert ins[-1] == -733

def f(is_part2=False):
    p = 0
    n_steps = 0
    while True:
        ip = ins[p]
        if ins[p] >= 3 and is_part2:
            ins[p] -= 1
        else:
            ins[p] += 1
        p += ip
        n_steps += 1
        # print(p, ins)
        if p < 0 or p >= len(ins):
            break
    return n_steps

print(f())
print(f(True))
