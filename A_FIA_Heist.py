def decode_string(s):
  decoded = []
  s_iter = iter(s)
  for char in s_iter:
    if char == "<":
      next(s_iter)
    if char == "<":
      if decoded:
        decoded.pop()
    else:
      decoded.append(char)
  return "".join(decoded)

# Read input
intercepted_string = input()

# Decode intercepted string
decoded_string = decode_string(intercepted_string)

# Print decoded string
print(decoded_string)
