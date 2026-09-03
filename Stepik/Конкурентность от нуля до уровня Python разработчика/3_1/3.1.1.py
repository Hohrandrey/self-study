import threading


def worker():
    print("worker")


def solution():
    # TODO: создайте поток, который печатает "worker",
    # запустите его и дождитесь завершения, затем напечатайте "done"
    t = threading.Thread(target=worker)
    t.start()
    t.join()
    print("done")


solution()
