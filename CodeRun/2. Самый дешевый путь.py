def main():
    n, m = map(int, input().split())
    matrix = []
    min_way = 10000

    for i in range(n):
        matrix.append(list(map(int, input().split())))

    res_matrix = [[0 for _ in range(m)] for _ in range(n)]
    res_matrix[0][0] = matrix[0][0]

    for i in range(1, m):
        res_matrix[0][i] = matrix[0][i] + res_matrix[0][i-1]

    for i in range(1, n):
        res_matrix[i][0] = matrix[i][0] + res_matrix[i-1][0]

    for i in range(1, n):
        for j in range(1, m):
            res_matrix[i][j] = min(res_matrix[i-1][j],res_matrix[i][j-1]) + matrix[i][j]

    print(res_matrix[-1][-1])

if __name__ == '__main__':
    main()