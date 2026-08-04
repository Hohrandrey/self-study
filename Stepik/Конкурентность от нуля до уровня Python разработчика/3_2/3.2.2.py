import threading

def solution():
    T, K = map(int, input().split())

    rlock = threading.RLock()
    data = []

    def inner(x):
        # TODO: взять rlock и добавить x в data
        with rlock:
            data.append(x)

    def outer(x):
        # TODO: взять rlock и вызвать inner(x)
        with rlock:
            inner(x)

    def worker(id_):
        for i in range(K):
            outer((id_, i))

    threads = [threading.Thread(target=worker, args=(t,)) for t in range(T)]
    for t in threads: t.start()
    for t in threads: t.join()

    print(len(data))

solution()