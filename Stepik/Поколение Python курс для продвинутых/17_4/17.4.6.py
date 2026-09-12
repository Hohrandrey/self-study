def concatenate_files(*args):
    with open('output.txt', 'w') as f:
        pass

    for arg in args:
        with open(arg, 'r') as f, open('output.txt', 'a', encoding='utf-8') as out:
            data = f.readlines()
            out.writelines(data)

concatenate_files('answer.txt', 'new_scores.txt')
with open('output.txt') as f:
    print(f.read())