numbers = [4.12, 1.3257, 9.37037, 4.552, 3.186]


def map(function, items):
    result = []
    for item in items:
        new_item = function(item, 2)
        result.append(new_item)

    return result


new_numbers = map(round, numbers)
print(*new_numbers, sep="\n")
