def solve():
    program = input()
    visited = {}
    x, y = 0, 0

    visited[(x, y)] = visited.get((x, y), 0) + 1

    for command in program:
        if command == 'U':
            y += 1
        elif command == 'D':
            y -= 1
        elif command == 'R':
            x += 1
        elif command == 'L':
            x -= 1

        visited[(x, y)] = visited.get((x, y), 0) + 1

    count_more_than_one = 0
    for visits in visited.values():
        if visits > 1:
            count_more_than_one += 1

    print(count_more_than_one)


if __name__ == "__main__":
    solve()