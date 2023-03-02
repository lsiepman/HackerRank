def mutate_string(string: str, position: int, character: str):
    """alter string based on index

    Args:
        string (str): string to be modified
        position (int): index to be modified
        character (str): new character to be inserted

    Returns:
        str: modified string
    """
    letters = list(string)
    letters[position] = character
    return "".join(letters)


if __name__ == "__main__":
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
