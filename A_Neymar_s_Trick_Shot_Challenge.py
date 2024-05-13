def count_bounces(N, X, lengths):
    position = 0
    bounces = 0
    for length in lengths:
        position += length
        if position <= X:
            bounces += 1
    return bounces + 1  # Add 1 for the initial bounce at D1=0
  
# Input
N, X = map(int, input().split())
lengths = list(map(int, input().split()))

# Output
print(count_bounces(N, X, lengths))