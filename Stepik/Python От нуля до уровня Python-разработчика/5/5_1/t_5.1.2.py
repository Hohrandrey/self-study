def gen_fibonacci():
    prev = 0
    cur = 1
    yield prev
    yield cur
    while True:
        prev, cur = cur, cur + prev
        yield cur

count = 0
for i in gen_fibonacci():
    print(i)
    count += 1
    if count == 10:
        break
