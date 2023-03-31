import numpy as np

if __name__ == "__main__":
    N = tuple(map(int, input().split()))
    print(np.zeros(N, dtype=np.int8))
    print(np.ones(N, dtype=np.int8))
