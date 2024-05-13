def largest_square_in_histogram(N, H):
    max_width = 0
    stack = []
    
    for i in range(N):
        height = None
        while stack and H[i] < H[stack[-1]]:
            height = H[stack.pop()]
        if height:
            width = i if not stack else i - stack[-1] - 1
            max_width = max(max_width, min(height, width))
        stack.append(i)
    
    while stack:
        height = H[stack.pop()]
        width = N if not stack else N - stack[-1] - 1
        max_width = max(max_width, min(height, width))
    
    return max_width

# Input
n = int(input())
h = list(map(int, input().split()))

# Output
print(largest_square_in_histogram(n, h))
