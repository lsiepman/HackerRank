import re


def check_valid(s):
    if re.search("^[A-Z]{5}[0-9]{4}[A-Z]$", s):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        check_valid(input())
