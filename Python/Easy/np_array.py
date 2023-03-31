import numpy as np


def arrays(arr):
    return np.flip(np.array(list(map(float, arr))))


arr = input().strip().split(" ")
result = arrays(arr)
print(result)
