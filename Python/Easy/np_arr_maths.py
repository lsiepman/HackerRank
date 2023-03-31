import numpy as np


def perform_task(A, B):
    print(np.add(A, B))
    print(np.subtract(A, B))
    print(np.multiply(A, B))
    print(np.floor_divide(A, B))
    print(np.mod(A, B))
    print(np.power(A, B))


if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    lst1 = []
    for _ in range(N):
        lst1.append(list(map(int, input().split())))

    lst2 = []
    for _ in range(N):
        lst2.append(list(map(int, input().split())))

    arr1 = np.array(lst1)
    arr2 = np.array(lst2)

    perform_task(arr1, arr2)
