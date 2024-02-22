# Условие
# 1. Напишите функцию для транспонирования матрицы

def transpose_matrix(matrix):
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            print(matrix[i][j],  end=' ')
        print()


matrix = [[6, 4, 2, 0], [7, 3, 4, 5]]


transpose_matrix(matrix)
