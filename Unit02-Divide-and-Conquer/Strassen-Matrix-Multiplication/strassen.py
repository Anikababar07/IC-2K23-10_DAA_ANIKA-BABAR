
def add_matrix(A, B):
    n = len(A)
    return [
        [A[i][j] + B[i][j] for j in range(n)]
        for i in range(n)
    ]


def subtract_matrix(A, B):
    n = len(A)
    return [
        [A[i][j] - B[i][j] for j in range(n)]
        for i in range(n)
    ]


def split_matrix(A):
    n = len(A)
    mid = n // 2

    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    return A11, A12, A21, A22


def combine_matrix(C11, C12, C21, C22):
    top = [C11[i] + C12[i] for i in range(len(C11))]
    bottom = [C21[i] + C22[i] for i in range(len(C21))]
    return top + bottom


def strassen(A, B):
    n = len(A)

    # Base case
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    A11, A12, A21, A22 = split_matrix(A)
    B11, B12, B21, B22 = split_matrix(B)

    # Calculate the seven products
    M1 = strassen(add_matrix(A11, A22),
                  add_matrix(B11, B22))

    M2 = strassen(add_matrix(A21, A22), B11)

    M3 = strassen(A11,
                  subtract_matrix(B12, B22))

    M4 = strassen(A22,
                  subtract_matrix(B21, B11))

    M5 = strassen(add_matrix(A11, A12), B22)

    M6 = strassen(subtract_matrix(A21, A11),
                  add_matrix(B11, B12))

    M7 = strassen(subtract_matrix(A12, A22),
                  add_matrix(B21, B22))

    # Calculate the four result quadrants
    C11 = add_matrix(
        subtract_matrix(add_matrix(M1, M4), M5), M7
    )

    C12 = add_matrix(M3, M5)
    C21 = add_matrix(M2, M4)

    C22 = add_matrix(
        add_matrix(subtract_matrix(M1, M2), M3), M6
    )

    return combine_matrix(C11, C12, C21, C22)


def next_power_of_two(n):
    power = 1
    while power < n:
        power *= 2
    return power


def strassen_multiply(A, B):
    n = len(A)

    if n == 0 or any(len(row) != n for row in A):
        raise ValueError("Matrix A must be a non-empty square matrix.")

    if len(B) != n or any(len(row) != n for row in B):
        raise ValueError("Matrix B must have the same square dimensions.")

    size = next_power_of_two(n)

    # Pad matrices with zeros
    padded_A = [
        row + [0] * (size - n) for row in A
    ] + [[0] * size for _ in range(size - n)]

    padded_B = [
        row + [0] * (size - n) for row in B
    ] + [[0] * size for _ in range(size - n)]

    result = strassen(padded_A, padded_B)

    # Remove padding
    return [row[:n] for row in result[:n]]


def read_matrix(name, n):
    print(f"Enter elements of Matrix {name}, row by row:")

    matrix = []

    for i in range(n):
        while True:
            try:
                row = list(map(
                    int,
                    input(f"Row {i + 1}: ").split()
                ))

                if len(row) != n:
                    print(f"Please enter exactly {n} integers.")
                    continue

                matrix.append(row)
                break

            except ValueError:
                print("Invalid input! Enter integers only.")

    return matrix


def main():
    try:
        n = int(input("Enter the order of square matrices: "))

        if n <= 0:
            print("Matrix order must be positive.")
            return

        A = read_matrix("A", n)
        B = read_matrix("B", n)

        result = strassen_multiply(A, B)

        print("\nMatrix A:")
        for row in A:
            print(row)

        print("\nMatrix B:")
        for row in B:
            print(row)

        print("\nResult using Strassen's Algorithm:")
        for row in result:
            print(row)

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
