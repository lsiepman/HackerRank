def compareTriplets(a, b):
    score1 = 0
    score2 = 0

    for idx in range(len(a)):
        if a[idx] > b[idx]:
            score1 += 1
        elif a[idx] < b[idx]:
            score2 += 1

    return [score1, score2]


if __name__ == "__main__":
    print("enter space separated triplets")
    a = list(map(int, input("triplet 1: ").rstrip().split()))
    b = list(map(int, input("triplet 2: ").rstrip().split()))

    print(compareTriplets(a, b))
