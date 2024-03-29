def staircase(n):
    b = n
    a = 0
    while a < n:
        b -= 1
        a += 1
        print(f"{' ' * b}{'#' * a}")


if __name__ == "__main__":
    n = int(input("Please input an integer \n").strip())

    staircase(n)
