import threading

def solution():
    T, K = map(int, input().split())

    counter = 0
    lock = threading.Lock()

    def worker():
        nonlocal counter
        with lock:
            for i in range(K):
                counter += 1

    threads = [threading.Thread(target=worker) for _ in range(T)]
    for t in threads: t.start()
    for t in threads: t.join()

    print(counter)

solution()