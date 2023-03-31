import numpy as np

if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    inp = []
    for _ in range(N):
        inp.append(list(map(int, input().split())))

    arr = np.array(inp)
    s = np.min(arr, axis=1)
    print(np.max(s))
