from collections import OrderedDict

if __name__ == "__main__":
    N = int(input())
    dct = OrderedDict()
    for _ in range(N):
        inp = input().split()
        y = inp.pop()
        x = " ".join(inp)
        if x in dct.keys():
            dct[x] += int(y)
        else:
            dct[x] = int(y)

    for k, v in dct.items():
        print(f"{k} {v}")
