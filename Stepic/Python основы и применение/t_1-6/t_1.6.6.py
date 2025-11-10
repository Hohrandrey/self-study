import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def append(self, __object, msg):
        super(LoggableList, self).append(__object)
        self.log(msg)

ct = LoggableList([1, 2, 3])
print(ct)
ct.append(4, "rj")