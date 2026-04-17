s = input().strip()
n = len(s)

if n == 0:
    print("YES")
elif n % 2 != 0:
    print("NO")
else:

    def is_valid(seq):
        stack = []
        pairs = {")": "(", "]": "[", "}": "{"}
        for c in seq:
            if c in "([{":
                stack.append(c)
            else:
                if not stack or stack[-1] != pairs[c]:
                    return False
                stack.pop()
        return len(stack) == 0

    found = False
    for k in range(n):
        shifted = s[k:] + s[:k]
        if is_valid(shifted):
            found = True
            break

    print("YES" if found else "NO")
