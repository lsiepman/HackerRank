def swap_case(s):
    """swap case of strings

    Args:
        s (str): text that needs to be case-swapped
    Returns:
        str: Case-swapped text
    """
    return s.swapcase()


if __name__ == "__main__":
    s = input()
    result = swap_case(s)
    print(result)
