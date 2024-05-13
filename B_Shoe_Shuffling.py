from itertools import count

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    temp = list(range(1, n+1))
    i = 0
    while i < n:
        cnt = 1
        while i < n - 1 and arr[i] == arr[i+1]:
            temp[i], temp[i+1] = temp[i+1], temp[i]
            i += 1
            cnt += 1
        if cnt == 1:
            print(-1)
            flag = False
            break
        i += 1
    if not flag:
        continue
    print(*temp)
