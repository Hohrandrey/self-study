import threading


def solution():
    n = int(input().strip())
    arr = list(map(int, input().split()))
    arr = arr[:n]

    result = {"sum": 0}

    # TODO: создайте поток, который посчитает сумму arr и запишет в result["sum"]
    # Запустите поток, дождитесь завершения, затем выведите сумму.

    def summ():
        result["sum"] = sum(arr)

    t = threading.Thread(target=summ)
    t.start()
    t.join()
    print(result["sum"])


solution()
