def max_not_disappointed_drivers(n, ti):
    # Sort the list of tuples
    ti.sort()

    max_wait_time = 0
    not_disappointed = 0

    # Iterate through the sorted list of tuples
    for i in range(n):
        # Update the maximum wait time
        if ti[i] >= max_wait_time:
            max_wait_time += ti[i]
            # If the index of the current car is less than or equal to the maximum wait time
            # Increment not_disappointed
            not_disappointed += 1
    
    return not_disappointed

# Read input
n = int(input())
ti = list(map(int, input().split()))

# Calculate and print the maximum number of not disappointed drivers
print(max_not_disappointed_drivers(n, ti))
