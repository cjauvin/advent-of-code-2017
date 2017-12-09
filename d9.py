def f(s):
    n_groups = 0
    score = 0
    n_garbage_chars = 0
    level = 0
    is_garbage = False
    is_ignore = False
    for c in s:
        if is_ignore:
            is_ignore = False
            continue
        if not is_garbage:
            if c == '{':
                n_groups += 1
                level += 1
                score += level
            elif c == '}':
                level -= 1
        else:
            if c not in ('>', '!'):
                n_garbage_chars += 1
        if c == '!':
            is_ignore = True
        elif c == '<':
            is_garbage = True
        elif c == '>':
            is_garbage = False
    return n_groups, score, n_garbage_chars

assert f('{}')[0] == 1
assert f('{{{}}}')[0] == 3
assert f('{{},{}}')[0] == 3
assert f('{{{},{},{{}}}}')[0] == 6
assert f('{<{},{},{{}}>}')[0] == 1
assert f('{<a>,<a>,<a>,<a>}')[0] == 1
assert f('{{<a>},{<a>},{<a>},{<a>}}')[0] == 5
assert f('{{<!>},{<!>},{<!>},{<a>}}')[0] == 2

assert f('{}')[1] == 1
assert f('{{{}}}')[1] == 6
assert f('{{},{}}')[1] == 5
assert f('{{{},{},{{}}}}')[1] == 16
assert f('{<a>,<a>,<a>,<a>}')[1] == 1
assert f('{{<ab>},{<ab>},{<ab>},{<ab>}}')[1] == 9
assert f('{{<!!>},{<!!>},{<!!>},{<!!>}}')[1] == 9
assert f('{{<a!>},{<a!>},{<a!>},{<ab>}}')[1] == 3

assert f('<>')[2] == 0
assert f('<random characters>')[2] == 17
assert f('<<<<>')[2] == 3
assert f('<{!>}>')[2] == 2
assert f('<!!>')[2] == 0
assert f('<!!!>>')[2] == 0
assert f('<{o"i!a,<{i<a>')[2] == 10

a = open('d9.txt').readlines()[0]
print(f(a))
