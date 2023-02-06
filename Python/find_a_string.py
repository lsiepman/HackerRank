def count_substring(string: str, sub_string: str):
    """Count the occurences of a substring in a string

    Also counts overlaps

    Args:
        string (str): string to be examined
        sub_string (str): substring to be found

    Returns:
        int: substring count
    """
    a = [i for i in range(len(string)) if string.startswith(sub_string, i)]
    return len(a)


if __name__ == "__main__":
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
