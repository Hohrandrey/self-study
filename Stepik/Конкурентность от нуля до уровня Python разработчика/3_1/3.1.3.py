import threading

class Demo(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)
        self.where = None

    def run(self):
        # TODO: сохранить имя текущего потока в self.where
        self.where = threading.current_thread().name

def solution():
    mode = input().strip()
    d = Demo(name="worker-1")

    if mode == "run":
        # TODO: вызвать run() напрямую и вывести self.where
        d.run()
        print(d.where)
    else:
        # TODO: вызвать start(), затем join(), и вывести self.where
        d.start()
        d.join()
        print(d.where)

solution()