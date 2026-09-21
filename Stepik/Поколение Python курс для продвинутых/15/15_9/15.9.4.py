print(all(map(lambda el: el.isdigit() and 0 <= int(el) <= 255, input().split("."))))
