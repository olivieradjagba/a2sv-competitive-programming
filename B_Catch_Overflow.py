def check_overflow(commands):
    stack = [1]
    x = 0
    limit = (1 << 32) - 1
    for command in commands:
        cmd = command.split()
        n = int(cmd[1]) if len(cmd) > 1 else 0 # Very important
        cmd = cmd[0]
        if cmd == 'for':
            next = stack[-1] * n
            stack.append(next if next <= limit else 0)
        elif stack and cmd == 'end':
            stack.pop()
        else:
            if stack[-1] == 0 or x + stack[-1] > limit:
                return "OVERFLOW!!!"
            x += stack[-1]
    return x

# Input processing
t = int(input())
commands = []
for _ in range(t):
    commands.append(input())

# Check for overflow and print result
result = check_overflow(commands)
print(result)
