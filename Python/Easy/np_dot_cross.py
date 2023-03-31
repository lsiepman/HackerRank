import numpy as np

if __name__ == "__main__":
    N = int(input())
    lst1 = []
    for _ in range(N):
        lst1.append(list(map(int, input().split())))

    lst2 = []
    for _ in range(N):
        lst2.append(list(map(int, input().split())))

    arr1 = np.array(lst1)
    arr2 = np.array(lst2)

    print(np.matmul(arr1, arr2))
