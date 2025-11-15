def solve():
    a, b = map(int, input().split())

    if a == b:
        print(0)
        return

    # 找最高有效位
    def msb(x):
        if x == 0:
            return -1
        pos = 0
        while (1 << (pos + 1)) <= x:
            pos += 1
        return pos

    msb_a = msb(a)
    msb_b = msb(b)

    if msb_b > msb_a:
        print(-1)
        return

    operations = []

    for i in range(msb_a):
        if a & (1 << i):
            x = 1 << i
            operations.append(x)
            a ^= x

    for i in range(msb_a + 1):
        bit_in_a = (a >> i) & 1
        bit_in_b = (b >> i) & 1

        if bit_in_a != bit_in_b:
            x = 1 << i
            operations.append(x)
            a ^= x

    print(len(operations))
    if operations:
        print(' '.join(map(str, operations)))


t = int(input())
for _ in range(t):
    solve()