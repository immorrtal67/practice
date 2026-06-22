def read_matrix_size():
    while True:
        try:
            n = int(input("Введите порядок квадратной матрицы (N): "))
            if n > 0:
                return n
            print("Ошибка: размерность должна быть положительным числом.")
        except ValueError:
            print("Ошибка: введите целое число.")


def read_matrix_row(size, row_index):
    while True:
        try:
            row = list(map(float, input(f"Строка {row_index}: ").split()))
            if len(row) != size:
                print(f"Ошибка: ожидается {size} чисел, введено {len(row)}.")
                continue
            return row
        except ValueError:
            print("Ошибка: допустимы только числа.")


def build_square_matrix(n):
    print(f"Введите элементы матрицы {n}x{n} (числа через пробел):")
    return [read_matrix_row(n, i + 1) for i in range(n)]


def get_submatrix(matrix, remove_row, remove_col):
    return [
        [value for col_idx, value in enumerate(row) if col_idx != remove_col]
        for row_idx, row in enumerate(matrix) if row_idx != remove_row
    ]


def calculate_determinant(matrix):
    n = len(matrix)

    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det_value = 0
    for col_idx in range(n):
        sign = 1 if col_idx % 2 == 0 else -1
        element = matrix[0][col_idx]
        minor = get_submatrix(matrix, 0, col_idx)

        det_value += sign * element * calculate_determinant(minor)

    return det_value

def format_result(value):
    return int(value) if value.is_integer() else value

def main():
    try:
        size = read_matrix_size()
        matrix = build_square_matrix(size)

        result = calculate_determinant(matrix)
        print(f"Определитель равен: {format_result(result)}")

    except KeyboardInterrupt:
        print("Программа прервана пользователем.")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")

if __name__ == "__main__":
    main()