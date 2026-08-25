inp_list = sorted(map(int, input().split()))

def sort_by_sum(num):
    return sum(map(int, str(num)))

print(*sorted(inp_list, key=sort_by_sum))