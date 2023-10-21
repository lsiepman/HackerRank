import re


def check_valid(s):
    if re.search("^[a-z]{,3}[0-9]{2,8}[A-Z]{3,}$", s):
        print("VALID")
    else:
        print("INVALID")


if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        check_valid(input())
