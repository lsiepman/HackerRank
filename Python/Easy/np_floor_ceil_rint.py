import numpy as np

np.set_printoptions(legacy="1.13")

if __name__ == "__main__":
    inp = list(map(float, input().split()))
    arr = np.array(inp)
    print(np.floor(arr))
    print(np.ceil(arr))
    print(np.rint(arr))
