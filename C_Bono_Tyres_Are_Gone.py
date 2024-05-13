def min_reorderings(n, commands):
    stack = []
    expected_tire = 1
    reorder_count = 0

    for command in commands:
        if command[0] == "add":
            stack.append(int(command[1]))
        else:  # command is "remove"
            if stack and stack[-1] == expected_tire:
                stack.pop()
                expected_tire += 1
            else:
                reorder_count += 1

    return reorder_count

# Input parsing
n = int(input())
commands = [input().split() for _ in range(2 * n)]

# Calculate and print the result
print(min_reorderings(n, commands))
