import re


def check_text(s):
    ip6 = (
        r"^[0-9a-fA-F]{0,4}:[0-9a-fA-F]{0,4}:[0-9a-fA-F]{0,4}:[0-9a-fA-F]"
        r"{0,4}:[0-9a-fA-F]{0,4}:[0-9a-fA-F]{0,4}:[0-9a-fA-F]{0,4}:"
        r"[0-9a-fA-F]{0,4}$"
    )
    ip4 = r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$"

    if re.search(ip6, s):
        print("IPv6")
    elif re.search(ip4, s) and all(
        int(i) <= 255 for i in re.findall(ip4, s)[0]
    ):
        print("IPv4")
    else:
        print("Neither")


if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        check_text(input().strip())
