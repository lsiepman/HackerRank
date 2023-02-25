# Complete the solve function below.
import string


def solve(s):
    return string.capwords(s, " ")


if __name__ == "__main__":
    s = input()

    result = solve(s)

    print(result)
