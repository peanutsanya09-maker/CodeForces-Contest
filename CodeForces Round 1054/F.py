def solve():
    h,d = map(int,input().split())

    def T(t):
        return t*(t+1) // 2

    def C(m):
        s = m + 1
        a = d//s
        r = d%s

        # r段长度a+1, (s-r)段长度a
        cost = r*T(a+1) + (s-r)*T(a)
        return cost

    def check(m):
        return C(m) <= h+m - 1

    l,r = 0,d
    ans = d
    while l <= r:
        mid = (l + r)//2
        if check(mid):
            ans= mid
            r = mid - 1
        else:
            l = mid + 1
    print(d + ans)
t = int(input())
for _ in range(t):
    solve()