import re


def check_hi(s):
    if re.search("^[Hh][Ii] [^Dd]", s):
        print(s)


if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        check_hi(input())
