def min_strength_difference(n, strengths):
    strengths.sort()  # Sort the strengths in ascending order
    min_difference = float('inf')  # Initialize minimum difference to positive infinity
    
    for i in range(1, n):
        team_A = strengths[:i]  # Athletes in team A
        team_B = strengths[i:]  # Athletes in team B
        difference = max(team_A) - min(team_B)  # Calculate the difference
        min_difference = min(min_difference, difference)  # Update minimum difference
    
    return min_difference

# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read input for the current test case
    n = int(input())  # Number of athletes
    strengths = list(map(int, input().split()))  # Strengths of athletes
    
    # Calculate and print the minimum strength difference
    print(min_strength_difference(n, strengths))
