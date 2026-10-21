def main():
    def diploms(w,h,n):
        left = max(w, h)
        right = left * n

        while left + 1 < right:
            mid = (left + right) // 2
            res = (mid//w)*(mid//h)
            if res < n:
                left = mid
            else:
                right = mid

        return right

    print(diploms(3,4, 9))

if __name__ == '__main__':
    main()