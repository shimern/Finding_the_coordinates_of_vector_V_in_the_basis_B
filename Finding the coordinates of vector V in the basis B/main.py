import math


def Gauss(a, n):
    for i in range(n - 1):
        x = a[i][i]
        for j in range(i, n + 1):
            if a[i][j] != 0:
                a[i][j] = round((a[i][j] / x) * 10000000) / 10000000
            else:
                break

        for h in range(i + 1, n):
            x = a[h][i]
            for k in range(i, n + 1):
                a[h][k] = a[i][k] * (-x) + a[h][k]

    if a[n - 1][n - 1] != 0:
        a[n - 1][n] = round((a[n - 1][n] / a[n - 1][n - 1]) * 10000000) / 10000000
    a[n - 1][n - 1] = 1


def main():
    m = []
    v = []
    n = int(input("Введите размерность матрицы: "))

    print("Введите вектор:")
    for j in range(n):
        x = float(input())
        v.append(x)

    print("Введите матрицу базиса:")
    for i in range(n):
        tmp = []
        for j in range(n):
            x = float(input())
            tmp.append(x)
        m.append(tmp)

    mr = m
    for i in range(n):
        mr[i].append(v[i])

    Gauss(mr, n)

    f = True
    for i in range(n - 1):
        for j in range(i + 1, n):
            if mr[i][i] != mr[j][j]:
                f = False

    if f:
        mr[n - 1][n - 1] = mr[n - 1][n]
        for i in range(n - 2, -1, -1):
            mr[i][i] = mr[i][n]
            for j in range(n - 1, i, -1):
                mr[i][i] -= mr[i][j] * mr[j][j]

        print("\nКоординаты вектора в базисе:")
        for i in range(n):
            if mr[i][i] == -0 or mr[i][i] == +0:
                mr[i][i] = 0
            print(mr[i][i], end=" ")

    else:
        print("Невозможно определить координаты вектора в данном базисе.")


if __name__ == "__main__":
    main()