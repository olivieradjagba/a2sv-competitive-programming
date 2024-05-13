# Author: rishabhxchoudhary
# Created: 15.01.2024 20:21:34 (GMT+5:30)
# import sys
# sys.setrecursion_limit(2147483647)
# MOD = 1000000007
from collections import deque

def solve(n, m, a, b):
    a.sort()
    b.sort(reverse=True)
    # print(a, b)
    ans = 0
    check = -1
    for i in range(n):
        if abs(a[i] - b[-(n - i)]) > abs(a[i] - b[i]):
            check = i
            break
        ans += abs(a[i] - b[i])
        # print(a[i], b[i])
    if check != -1:
        for i in range(check, n):
            ans += abs(a[i] - b[-(n - i)])
            # print(a[i], b[-(n - i)])
    print(ans)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    solve(n, m, a, b)
