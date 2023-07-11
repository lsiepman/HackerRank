import re


def check_valid(s):
    t = re.search(r"^(\.|_)[0-9]+[a-zA-Z]*_?$", s)
    if t:
        print("VALID")
    else:
        print("INVALID")


if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        check_valid(input())
