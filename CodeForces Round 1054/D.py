def solve_for_char(s, target):

    pos = []
    for i in range(len(s)):
        if s[i] == target:
            pos.append(i)

    m = len(pos)

    if m == 0 or m == len(s):
        return 0


    b = []
    for i in range(m):
        b.append(pos[i] - i)


    b.sort()
    median = b[m // 2]


    cost = 0
    for bi in b:
        cost += abs(bi - median)

    return cost

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    print(min(solve_for_char(s, 'a'), solve_for_char(s, 'b')))