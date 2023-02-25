if __name__ == "__main__":
    n, m = [int(i) for i in input().split(" ")]

    mult = 1
    for i in range(n):
        if i < n // 2:
            print((".|." * mult).center(m, "-"))
            mult += 2
        elif i == n // 2:
            print("WELCOME".center(m, "-"))
        elif i > n // 2:
            mult -= 2
            print((".|." * mult).center(m, "-"))
