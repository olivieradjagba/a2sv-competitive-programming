def min_operations_to_sort(n, s):
  stack = []
  for c in s:
    while stack and stack[-1] <= c:
      stack.pop()
    stack.append(c)
  return len(stack)

t = int(input())
for _ in range(t):
  n = int(input().strip())
  s = input().strip()
  print(min_operations_to_sort(n, s))
