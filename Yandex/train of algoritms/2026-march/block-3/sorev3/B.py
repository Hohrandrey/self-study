import sys


def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    iterator = iter(data)
    try:
        N = int(next(iterator))
        K = int(next(iterator))
    except StopIteration:
        return

    a = []
    for _ in range(N):
        try:
            a.append(int(next(iterator)))
        except StopIteration:
            break

    if K == 1:
        sys.stdout.write("0")
        return

    INF = float('inf')
    min_prefix = [INF] * K
    min_prefix[0] = 0
    global_min_val = 0
    global_min_rem = 0
    second_min_val = INF
    second_min_rem = -1

    best_sum = 0
    prefix_sum = 0

    mp = min_prefix

    for i in range(N):
        prefix_sum += a[i]
        r = prefix_sum % K

        if r != global_min_rem:
            min_other_val = global_min_val
        else:
            min_other_val = second_min_val

        if min_other_val != INF:
            candidate = prefix_sum - min_other_val
            if candidate > best_sum:
                best_sum = candidate

        if prefix_sum < mp[r]:
            mp[r] = prefix_sum
            if r == global_min_rem:
                global_min_val = prefix_sum
            else:
                if prefix_sum < global_min_val:
                    second_min_val = global_min_val
                    second_min_rem = global_min_rem

                    global_min_val = prefix_sum
                    global_min_rem = r
                else:
                    if r == second_min_rem:
                        second_min_val = prefix_sum
                    else:
                        if prefix_sum < second_min_val:
                            second_min_val = prefix_sum
                            second_min_rem = r

    if best_sum < 0:
        best_sum = 0

    sys.stdout.write(str(best_sum))


if __name__ == "__main__":
    solve()