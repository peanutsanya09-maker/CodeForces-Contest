from collections import defaultdict
t = int(input())
def solve():
    n,k,l,r = map(int,input().split())
    a = list(map(int,input().split()))

    #x:恰好有k个
    #y:至多有k个
    cnt_x = defaultdict(int)
    cnt_y = defaultdict(int)
    ans = 0
    x = 0
    y = 0
    for i in range(n):

        if i > 0:
            cnt_x[a[i-1]] -= 1
            cnt_y[a[i-1]] -= 1
            if cnt_x[a[i-1]] == 0:
                del cnt_x[a[i-1]]
            if cnt_y[a[i-1]] == 0:
                del cnt_y[a[i-1]]


        while x < n and len(cnt_x) < k:
            cnt_x[a[x]] += 1
            x += 1

        if len(cnt_x) < k:
            break

        while y < x:
            cnt_y[a[y]] += 1
            y += 1

        while y < n:
            cnt_y[a[y]] += 1
            if len(cnt_y) > k:
                cnt_y[a[y]] -= 1
                if cnt_y[a[y]] == 0:
                    del cnt_y[a[y]]
                break
            y += 1

        left = max(l + i -1,x-1)
        right = min(r + i -1,y-1)
        if left <= right:
            ans += right - left + 1

    print(ans)

for _ in range(t):
    solve()

