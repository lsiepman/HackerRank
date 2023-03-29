cube = lambda x: x * x * x


def fibonacci(n):
    res = [0]
    first_num = 1
    if n == 0:
        return []

    elif n == 1:
        return res

    res.append(first_num)
    if n == 2:
        return res

    for _ in range(n - 2):
        res.append(res[-1] + res[-2])

    return res


if __name__ == "__main__":
    n = int(input())
    print(list(map(cube, fibonacci(n))))
