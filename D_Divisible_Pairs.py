def divisible_pairs(n, x, y, v):
  mp = {}  # Initialize map
  ans = 0
  for i in range(n):
    a = v[i] % x
    b = v[i] % y
    p = ((x - a) + x) % x
    q = ((y + b) + y) % y
    ans += mp.get((p, q), 0)
    mp[(a, b)] = mp.get((a, b), 0) + 1
  return ans

if __name__ == "__main__":
  t = int(input())
  for _ in range(t):
    n, x, y = map(int, input().split())
    v = list(map(int, input().split()))
    print(divisible_pairs(n, x, y, v))
