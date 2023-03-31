import numpy as np

if __name__ == "__main__":
    N, M, P = list(map(int, input().split()))
    lst1 = []
    for _ in range(N):
        lst1.append(list(map(int, input().split())))

    lst2 = []
    for _ in range(M):
        lst2.append(list(map(int, input().split())))

    arr1 = np.array(lst1)
    arr2 = np.array(lst2)

    print(np.concatenate((arr1, arr2)))
