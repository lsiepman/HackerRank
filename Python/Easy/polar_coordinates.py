import cmath
import re


def process_input(inp):
    processing = re.search(r"^(\-?[0-9]+)\+*(\-?[0-9]+)j$", inp)
    val1 = int(processing.group(1))
    val2 = int(processing.group(2))
    return val1, val2


if __name__ == "__main__":
    inp = input()
    x, y = process_input(inp)

    phi = cmath.phase(complex(x, y))
    r = abs(complex(x, y))

    print(r)
    print(phi)
