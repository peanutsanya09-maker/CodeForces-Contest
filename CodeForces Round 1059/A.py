t = int(input())

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    print(max(a))

for _ in range(t):
    solve()