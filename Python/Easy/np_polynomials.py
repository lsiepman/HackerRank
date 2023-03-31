import numpy as np

if __name__ == "__main__":
    arr = np.array(list(map(float, input().split())))
    x = float(input())
    print(np.polyval(arr, x))
