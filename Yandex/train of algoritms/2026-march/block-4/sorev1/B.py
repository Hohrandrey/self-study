import sys


def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    first_line = input_data[0].split()
    if len(first_line) != 3:
        return

    try:
        n = int(first_line[0])
        m = int(first_line[1])
        k = int(first_line[2])
    except ValueError:
        return

    if n < 0 or m < 0 or k < 0:
        print(-2)
        return

    windows = [""] * n
    current_window_idx = 0
    clipboard = ""

    commands = []
    for i in range(1, min(m + 1, len(input_data))):
        commands.append(input_data[i].strip())

    for cmd in commands:
        if cmd == "Next":
            current_window_idx = (current_window_idx + 1) % n
        elif cmd == "Backspace":
            if windows[current_window_idx]:
                windows[current_window_idx] = windows[current_window_idx][:-1]
        elif cmd == "Copy":
            content = windows[current_window_idx]
            if len(content) > k:
                clipboard = content[-k:]
            else:
                clipboard = content
        elif cmd == "Paste":
            windows[current_window_idx] += clipboard
        elif len(cmd) == 1 and 'a' <= cmd <= 'z':
            windows[current_window_idx] += cmd

    final_content = windows[current_window_idx]
    if not final_content:
        print("Empty")
    else:
        if len(final_content) > k:
            print(final_content[-k:])
        else:
            print(final_content)


if __name__ == "__main__":
    solve()