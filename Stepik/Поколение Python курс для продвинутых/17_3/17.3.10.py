dict_files = {}

for _ in range(int(input())):
    file_name = input()
    with open(file_name, encoding='utf-8') as f:
        file = f.read()

    dict_files[file_name] = file.count('\n') + len(file.replace('\n', ''))

for el in sorted(sorted(dict_files), key=lambda k: dict_files[k], reverse=True):
    print(el, f'{dict_files[el]}B')