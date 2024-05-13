def max_good_subrectangle_area(n, m, table):
    # Initialize prefix sum array
    prefix_sum = [[0] * m for _ in range(n)]
    
    # Construct prefix sum array
    for i in range(n):
        for j in range(m):
            if table[i][j] == '1':
                prefix_sum[i][j] = prefix_sum[i-1][j] + 1 if i > 0 else 1
    
    # Calculate maximum area of good sub-rectangle
    max_area = 0
    for i in range(n):
        for j in range(m):
            if table[i][j] == '1':
                min_height = prefix_sum[i][j]
                width = 1
                for k in range(j-1, -1, -1):
                    min_height = min(min_height, prefix_sum[i][k])
                    width += 1
                    max_area = max(max_area, min_height * width)
    
    return max_area

# Read input
n, m = map(int, input().split())
table = [input() for _ in range(n)]

# Calculate and print the maximum area of a good sub-rectangle
print(max_good_subrectangle_area(n, m, table))
