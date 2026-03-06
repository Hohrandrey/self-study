def gen_range(start, end):
    for i in range (start, end):
        yield i


def gen_symbols():
    for elem in ['@', '#', '%']:
        yield elem


def chain():
    yield from gen_range(1, 4)
    yield from gen_symbols()


for elem in chain():
    print(elem)
