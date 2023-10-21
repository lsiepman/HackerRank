import re


def split_num(s):
    reg = re.search(r"^([0-9]{1,3})[\s\-]([0-9]{1,3})[\s\-]([0-9]{4,10})$", s)
    cc = reg.group(1)
    lc = reg.group(2)
    nm = reg.group(3)
    print(f"CountryCode={cc},LocalAreaCode={lc},Number={nm}")


if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        split_num(input())
