def solution(text, ending):
    flag = True
    if text[-2:] != ending:
        flag = False
    print(flag)
