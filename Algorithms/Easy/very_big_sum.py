def aVeryBigSum(ar):
    return int(sum(ar))


if __name__ == "__main__":
    ar_count = int(input("Array length: ").strip())
    ar = list(map(int, input("Array: ").rstrip().split()))
    print(aVeryBigSum(ar))
