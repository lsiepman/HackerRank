import numpy as np

np.set_printoptions(legacy="1.13")

if __name__ == "__main__":
    N, M = map(int, input().split())
    inp = []
    for _ in range(N):
        inp.append(list(map(int, input().split())))

    arr = np.array(inp)
    print(np.mean(arr, axis=1))
    print(np.var(arr, axis=0))
    print(np.round(np.std(arr), 11))
