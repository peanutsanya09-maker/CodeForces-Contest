import random
from collections import defaultdict
from bisect import bisect_left, bisect_right


def solve():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    # 预处理:记录每个值的所有位置
    positions = defaultdict(list)
    for i in range(n):
        positions[a[i]].append(i + 1)  # 1-indexed

    for _ in range(q):
        l, r = map(int, input().split())
        length = r - l + 1
        threshold = length // 3

        # 随机采样 k 次
        k = 50
        candidates = set()

        for _ in range(k):
            # 随机选一个位置
            rand_pos = random.randint(l, r)
            candidates.add(a[rand_pos - 1])  # 转为0-indexed

        # 验证每个候选
        result = []

        for cand in candidates:
            # 二分查找 cand 在 [l, r] 中的出现次数
            pos_list = positions[cand]

            left_idx = bisect_left(pos_list, l)

            right_idx = bisect_right(pos_list, r)

            count = right_idx - left_idx

            if count > threshold:
                result.append(cand)

        result.sort()

        if result:
            print(' '.join(map(str, result)))
        else:
            print(-1)


t = int(input())
for _ in range(t):
    solve()