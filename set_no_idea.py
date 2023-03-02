if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))

    num = 0

    for i in arr:
        if i in A:
            num += 1

        if i in B:
            num -= 1

    print(num)
