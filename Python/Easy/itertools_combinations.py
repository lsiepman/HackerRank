from itertools import combinations

if __name__ == "__main__":
    s, n = input().split()
    n = int(n)
    s = sorted(s)
    res = []
    for idx in range(1, n + 1):
        res.extend(list(combinations(s, idx)))

    for i in res:
        print("".join(i))
