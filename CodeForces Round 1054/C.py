t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    present = set(x for x in a if x < k)
    missing = k - len(present)
    count_k = a.count(k)

    print(max(missing, count_k))

