import numpy as np
from collections import Counter

s = """
../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#
"""

# https://stackoverflow.com/a/16858283/787842
def blockshaped(arr, nrows):#, ncols):
    """
    Return an array of shape (n, nrows, ncols) where
    n * nrows * ncols = arr.size

    If arr is a 2D array, the returned array should look like n subblocks with
    each subblock preserving the "physical" layout of arr.
    """
    h, w = arr.shape
    ncols = nrows
    return (arr.reshape(h//nrows, nrows, -1, ncols)
               .swapaxes(1,2)
               .reshape(-1, nrows, ncols))

# https://stackoverflow.com/a/16873755/787842
def unblockshaped(arr, h): #, w):
    """
    Return an array of shape (h, w) where
    h * w = arr.size

    If arr is of shape (n, nrows, ncols), n sublocks of shape (nrows, ncols),
    then the returned array preserves the "physical" layout of the sublocks.
    """
    n, nrows, ncols = arr.shape
    w = h
    return (arr.reshape(h//nrows, -1, nrows, ncols)
               .swapaxes(1,2)
               .reshape(h, w))

def get_variants(a):
    for x in [-1, 0, 1]:
        for k in range(4):
            if x == -1: # dont flip
                yield np.rot90(a, k=k)
            else:
                yield np.rot90(np.flip(a, x), k=k)

rules = {} # np.array.tobytes() -> np.array

for l in open('d21.txt'):
#for l in s.split('\n'):
    if not l.strip(): continue
    left, right = l.split('=>')
    left = np.asarray([list(row) for row in left.strip().split('/')])
    right = np.asarray([list(row) for row in right.strip().split('/')])
    for v in get_variants(left):
        rules[v.tobytes()] = right

p = np.asarray((list('.#.'), list('..#'), list('###')))

n_iters = 5 # part1
#n_iters = 18

print()

for _ in range(n_iters):
    # 2x2 -> 3x3
    if p.shape[0] % 2 == 0:
        q = blockshaped(p, 2)
        qqs = []
        for qq in q:
            assert set(qq.shape) == {2}
            #print(qq.shape)
            qqs.append(rules[qq.tobytes()])
        p = unblockshaped(np.asarray(qqs), int(np.sqrt(len(qqs))) * 3)
        print(p.shape)
        continue
    # 3x3 -> 4x4
    assert p.shape[0] % 3 == 0
    q = blockshaped(p, 3)
    qqs = []
    for qq in q:
        assert set(qq.shape) == {3}
        qqs.append(rules[qq.tobytes()])
    p = unblockshaped(np.asarray(qqs), int(np.sqrt(len(qqs))) * 4)
    print(p.shape)

print(Counter(p.flatten()))
