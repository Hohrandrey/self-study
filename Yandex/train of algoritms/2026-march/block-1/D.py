import sys


def main():
    troom, tcond = map(int, input().split())
    mode = input()
    match mode:
        case "freeze":
            if troom <= tcond:
                print(troom)
            else:
                print(tcond)
        case "heat":
            if troom >= tcond:
                print(troom)
            else:
                print(tcond)
        case "auto":
            print(tcond)
        case "fan":
            print(troom)


if __name__ == "__main__":
    main()
