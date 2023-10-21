import re


def find_hackerrank(s):
    if re.search("^hackerrank.*hackerrank$", s) or re.search("^hackerrank$", s):
        print(0)
    elif re.search("^hackerrank", s):
        print(1)
    elif re.search("hackerrank$", s):
        print(2)
    else:
        print(-1)


if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        find_hackerrank(input())
