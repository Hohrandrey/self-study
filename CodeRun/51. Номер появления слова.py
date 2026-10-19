def main():
    dic = {}
    ans = ''

    with open("51. Номер появления слова.txt", 'r', encoding='utf-8') as f:
        # улучшить и сделать 1м фором
        for line in f.readlines():
            line = list(line.split())
            for el in line:
                dic[el] = dic.get(el, -1) + 1
                ans += str(dic[el]) + ' '
            print(line)

    print(ans[:-1])

if __name__ == '__main__':
    main()
