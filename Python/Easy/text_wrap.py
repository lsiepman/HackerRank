import textwrap


def wrap(string, max_width):
    lines = textwrap.wrap(string, max_width)
    multi_lines = "{}".format("\n".join(lines))
    return multi_lines


if __name__ == "__main__":
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
