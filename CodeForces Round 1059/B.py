t = int(input())


def solve():
    n = int(input())
    s = input()

    ones = [i + 1 for i in range(n) if s[i] == '1']

    print(len(ones))
    if ones:  # 非空列表为 True
        print(' '.join(map(str, ones)))


for _ in range(t):
    solve()
