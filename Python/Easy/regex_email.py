import re
from email.utils import parseaddr


if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        inp = input().strip()
        cleaned = parseaddr(inp)
        e = re.search(
            r"^[A-Za-z][A-Za-z0-9._-]+@[A-Za-z]+\.[A-Z|a-z]{1,3}$",
            cleaned[1],
        )
        if e:
            print(inp)
