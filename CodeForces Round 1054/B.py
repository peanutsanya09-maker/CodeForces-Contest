t = int(input())


def solve():
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    max_diff1 = 0
    for i in range(0, n, 2):
        max_diff1 = max(max_diff1, a[i + 1] - a[i])

    max_diff2 = 0
    half = n // 2
    for i in range(half):
        max_diff2 = max(max_diff2, a[i + half] - a[i])

    print(min(max_diff1, max_diff2))


for _ in range(t):
    solve()