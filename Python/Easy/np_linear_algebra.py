import numpy as np

if __name__ == "__main__":
    N = int(input())
    inp = []
    for _ in range(N):
        inp.append(list(map(float, input().split())))

    arr = np.array(inp)
    print(round(np.linalg.det(arr), 2))
