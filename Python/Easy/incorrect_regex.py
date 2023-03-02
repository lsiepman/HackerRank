import re


def validate_regex(regex):
    try:
        re.compile(regex)
        print(True)

    except re.error:
        print(False)


if __name__ == "__main__":
    n = int(input())
    strings = []
    for _ in range(n):
        strings.append(input())
    for i in strings:
        validate_regex(i)
