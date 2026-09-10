def main():
    string = input()

    if string == '':
        print(string)
        return

    c_el = {}
    for el in string:
        c_el[el] = c_el.get(el, 0) + 1

    lb = c_el.get('<', 0)
    rb = c_el.get('>', 0)
    sl = c_el.get('/', 0)

    if lb != rb or lb % 2 != 0 or sl != lb // 2 or lb == 0:
        print('Impossible')
        return

    pairs = sl

    chars = []
    for code in range(ord('a'), ord('z') + 1):
        char = chr(code)
        c = c_el.get(char, 0)
        if c % 2 != 0:
            print('Impossible')
            return
        elif c > 0:
            chars.append(char * (c // 2))

    print(chars)
    all_chars = ''.join(chars)

    if len(all_chars) < pairs:
        print('Impossible')
        return

    tags = []
    print(all_chars)
    for i in range(pairs - 1):
        tags.append(all_chars[i])

    print(tags)
    tags.append(all_chars[pairs - 1:])
    print(tags)

    tag_open = [f'<{t}>' for t in tags]
    tag_close = [f'</{t}>' for t in tags]

    print(''.join(tag_open) + ''.join(reversed(tag_close)))


if __name__ == '__main__':
    main()
