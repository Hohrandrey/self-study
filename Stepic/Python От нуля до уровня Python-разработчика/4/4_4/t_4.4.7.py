class TraceBlock:
    def __enter__(self):
        print("Вход в блок")
        return self


    def __exit__(self, exc_type, exc, tb):
        print("Выход из блока")


with TraceBlock():
    print("Работаем")
