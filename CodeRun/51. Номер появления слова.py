def main():
    dic = {}
    ans = ''

    with open("51. Номер появления слова.txt", 'r', encoding='utf-8') as f:
        for el in f.read().split():
            dic[el] = dic.get(el, -1) + 1
            ans += str(dic[el]) + ' '
    print(ans[:-1])

if __name__ == '__main__':
    main()
