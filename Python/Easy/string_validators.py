def has_alpha_num(s):
    return any(char.isalnum() for char in s)


def has_alpha(s):
    return any(char.isalpha() for char in s)


def has_numbers(s):
    return any(char.isdigit() for char in s)


def has_lower(s):
    return any(char.islower() for char in s)


def has_upper(s):
    return any(char.isupper() for char in s)


if __name__ == "__main__":
    s = input()
    print(has_alpha_num(s))
    print(has_alpha(s))
    print(has_numbers(s))
    print(has_lower(s))
    print(has_upper(s))
