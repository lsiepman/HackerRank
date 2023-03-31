import numpy as np

if __name__ == "__main__":
    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))

    arr1 = np.array(lst1)
    arr2 = np.array(lst2)

    print(np.inner(arr1, arr2))
    print(np.outer(arr1, arr2))
