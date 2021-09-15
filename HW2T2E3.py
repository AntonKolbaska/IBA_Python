from random import randrange


def matrix_q(matrix_x, n):  # Функция вывода матриц
    for i in range(n):
        for j in range(n):
            print(str(matrix_x[i][j]).rjust(3), end=' ')
        print()


n = int(input('Size: '))
matrix_a = [[int(k) for k in [randrange(-99, 100) for _ in range(n)]] for _ in range(n)]
matrix_b = [[int(k) for k in [randrange(-99, 100) for _ in range(n)]] for _ in range(n)]

print('\nMatrix A: ')
matrix_q(matrix_a, n)

print('\nMatrix B: ')
matrix_q(matrix_b, n)

print('\nMatrix A + B:')
for i in range(n):
    for j in range(n):
        print(str(matrix_a[i][j] + matrix_b[i][j]).rjust(4), end=" ")
    print()