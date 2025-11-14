from collections import Counter
t = int(input())

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    count = Counter(a)
    if count[-1] %2 == 0:
        print(count[0])
    else:
        print(count[0] + 2)
    return

for _ in range(t):
    solve()