class BaseLogger:
    def log(self):
        print('Сообщение')


class FileLogger(BaseLogger):
    def log(self):
        super().log()
        print("Сохранено в файл")


flog = FileLogger()
flog.log()
