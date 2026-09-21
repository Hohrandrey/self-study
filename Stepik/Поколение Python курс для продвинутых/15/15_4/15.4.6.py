inp_list = input().split()


def sort_by_sum(num):
    return sum(map(int, num))


print(*sorted(inp_list, key=sort_by_sum))
