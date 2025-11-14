from collections import defaultdict

t = int(input())
def solve():
    n,k,l,r = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0

    x = 0
    y = 0
    cnt_x = defaultdict(int)
    cnt_y = defaultdict(int)

    for i in range(n):
        if i > 0:
            cnt_x[a[i-1]] -= 1
            if cnt_x[a[i-1]] == 0:
                del cnt_x[a[i-1]]

                cnt_y[a[i-1]] -= 1
                if cnt_y[a[i-1]] == 0:
                    del cnt_y[a[i-1]]

        #维护x：恰好有k个不同的指针
        while x < n and len(cnt_x) < k:
            cnt_x[a[x]] += 1
            x += 1

        if len(cnt_x) < k:
            break

        y = max(x,y)
        while y < n:
            cnt_y[a[y]] += 1

            if len(cnt_y) > k:
                cnt_y[a[y]] -= 1
                if cnt_y[a[y]] == 0:
                    del cnt_y[a[y]]
                break
            y += 1
        left_bound = max(x-1,i+l-1)
        right_bound = min(y-1,i+r-1)

        if left_bound <= right_bound:
            count = right_bound - left_bound + 1
            ans += count
    print(ans)

for _ in range(t):
    solve()