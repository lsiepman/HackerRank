def avg(item):
    ans = sum(item) / len(item)
    return round(ans, ndigits=1)


if __name__ == "__main__":
    n, x = list(map(int, input().split()))
    marks = []
    for i in range(x):
        temp = list(map(float, input().split()))
        marks.append(temp)

    grouped = list(zip(*marks))
    for i in grouped:
        print(avg(i))
