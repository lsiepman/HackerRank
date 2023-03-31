import numpy as np

if __name__ == "__main__":
    inp = list(map(int, input().split()))
    my_arr = np.array(inp)
    print(my_arr.reshape((3, 3)))
