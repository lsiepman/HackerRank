import re


def validate_uid(string):
    # length and alphanumerics
    if not re.search(r"^[A-Za-z0-9]{10}$", string):
        print("Invalid")
        return

    # uniqueness
    if sorted(list(string)) != sorted(list(set(string))):
        print("Invalid")
        return

    # numerical and capital counts
    up_cnt = 0
    num_cnt = 0
    for letter in string:
        try:
            int(letter)
            num_cnt += 1
        except ValueError:
            if letter == letter.upper():
                up_cnt += 1

    if num_cnt < 3 or up_cnt < 2:
        print("Invalid")
        return

    # if all tests are passed
    print("Valid")


if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        s = input().strip()
        validate_uid(s)
