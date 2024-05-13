t = int(input())

for _ in range(t):
    n, a, b = map(int, input().split())
    
    # Calculate the cost for buying all yogurts individually
    cost_individual = n * a
    
    # Calculate the cost for buying yogurts in pairs with the promotion
    # Calculate the cost for the remaining yogurts if n is odd
    cost_pairs = (n // 2) * b + (n % 2) * a
    
    # Output the minimum cost
    print(min(cost_individual, cost_pairs))