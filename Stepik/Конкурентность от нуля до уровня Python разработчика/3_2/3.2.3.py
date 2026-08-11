import threading

def solution():
    n, c = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = arr[:n]

    cond = threading.Condition()
    buf = []
    total = 0

    def producer():
        # TODO: класть элементы arr в buf, ждать если len(buf) == c
        # после всех элементов положить None и уведомить
        with cond:
            for elem in arr:
                while len(buf) == c:
                    cond.wait()
                buf.append(elem)
                cond.notify()
            buf.append(None)
            cond.notify_all()


    def consumer():
        nonlocal total
        # TODO: забирать элементы из buf, ждать если пусто
        # встретив None — выйти
        while True:
            with cond:
                while not buf:
                    cond.wait()
                item = buf.pop(0)
                if item is None:
                    break
                total += item
                cond.notify()


    tp = threading.Thread(target=producer)
    tc = threading.Thread(target=consumer)
    tp.start(); tc.start()
    tp.join(); tc.join()
    print(total)

solution()