from collections import defaultdict

if __name__ == "__main__":
    d = defaultdict(list)
    n, m = map(int, input().split())

    for i in range(1, n + 1):
        d[input().strip()].append(i)

    for _ in range(m):
        inp = input().strip()
        if inp in d:
            print(*d[inp])

        else:
            print(-1)
