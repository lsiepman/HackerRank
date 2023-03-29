import re


def validate_phone_number(inp):
    if re.search(r"^[789]\d{9}$", inp):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        validate_phone_number(input().strip())
