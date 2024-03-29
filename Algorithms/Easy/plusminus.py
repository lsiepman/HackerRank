def plusMinus(arr):
    pos = [i for i in arr if i > 0]
    zero = [i for i in arr if i == 0]
    neg = [i for i in arr if i < 0]

    print(round(len(pos) / len(arr), 6))
    print(round(len(neg) / len(arr), 6))
    print(round(len(zero) / len(arr), 6))


if __name__ == "__main__":
    n = int(input("Array length: ").strip())

    arr = list(map(int, input("Array: ").rstrip().split()))

    plusMinus(arr)
