def diagonalDifference(arr):
    a = primary_diagonal(arr)
    b = secondary_diagonal(arr)
    return abs(a - b)


def primary_diagonal(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))


def secondary_diagonal(matrix):
    return sum(matrix[i][len(matrix) - i - 1] for i in range(len(matrix)))


if __name__ == "__main__":
    n = int(input("Array size: ").strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input("Array row: ").rstrip().split())))

    result = diagonalDifference(arr)

    print(result)
