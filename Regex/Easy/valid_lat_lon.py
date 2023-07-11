import re


def check_coords(s):
    coord = re.search(r"\(([0-9\-+.]+), ([0-9\-+.]+)\)", s)

    if not coord:
        print("Invalid")
        return

    try:
        x = coord.group(1)
        y = coord.group(2)

        leading_zero = r"^(\+|\-)?0[0-9]"

        if x[-1] == "." or y[-1] == ".":
            raise Exception("trailing .")

        elif re.search(leading_zero, x) or re.search(leading_zero, y):
            raise Exception("leading zero")

        xf = float(x)
        yf = float(y)

        if -90 <= xf <= +90 and -180 <= yf <= 180:
            print("Valid")
        else:
            print("Invalid")

    except:
        print("Invalid")


if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        check_coords(input())
