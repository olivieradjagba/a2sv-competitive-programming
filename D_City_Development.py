def constructSkyscrapers(n, limits):
    dp = [0] * (n + 1)
    ans = [0] * n

    for i in range(1, n + 1):
        for j in range(i):
            if limits[i - 1] >= limits[j]:
                dp[i] = max(dp[i], dp[j] + limits[i - 1])

    # Reconstruct the solution
    cur = dp.index(max(dp))
    for i in range(n - 1, -1, -1):
        if dp[i] == cur:
            ans[i] = limits[i]
            cur -= limits[i]

    return ans

# Input
n = int(input())
limits = list(map(int, input().split()))

# Output
result = constructSkyscrapers(n, limits)
print(*result)
