import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def append(self, element):
        super(LoggableList, self).append(element)
        self.log(element)

ct = LoggableList([1, 2, 3])
print(ct)
ct.append(4)