import numpy as np

if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    lst = []
    for _ in range(N):
        lst.append(list(map(int, input().split())))
    arr = np.array(lst)
    print(arr.transpose())
    print(arr.flatten())
