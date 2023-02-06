def split_and_join(line: str):
    """Split a string on a space, join it on a hyphen

    Args:
        line (str): line to be split and joined

    Returns:
        str: line after split and join
    """
    words = line.strip().split(" ")
    return "-".join(words)


if __name__ == "__main__":
    line = input()
    result = split_and_join(line)
    print(result)
