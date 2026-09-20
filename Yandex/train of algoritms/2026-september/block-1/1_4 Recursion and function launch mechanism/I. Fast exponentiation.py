import sys
sys.setrecursionlimit(100000)

def power(a,n):
    if n == 0:
        return 1
    elif n == 1:
        return a
    elif n % 2 == 0:
        return power(a**2,n//2)
    else:
        return a * power(a,n-1)

def main():
    a=int(input())
    n=int(input())
    print(power(a,n))

if __name__ == '__main__':
    main()
