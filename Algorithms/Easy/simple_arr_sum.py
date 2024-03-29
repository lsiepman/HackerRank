def simpleArraySum(ar):
    return int(sum(ar))


if __name__ == "__main__":
    ar_count = int(input("Array length: ").strip())

    ar = list(map(int, input("Array (' ' separated ints): ").rstrip().split()))

    result = simpleArraySum(ar)

    print(result)
