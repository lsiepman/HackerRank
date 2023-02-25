import string


def print_rangoli(size):
    letters = list(string.ascii_lowercase)[:size]
    letters.reverse()

    temp = []
    idx = 0
    storage = {}
    for i in letters:
        reversed_temp = list(reversed(temp))
        temp.append(i)
        if len(temp) > 1:
            row = temp + reversed_temp
        else:
            row = temp
        print("-".join(row).center(size * 4 - 3, "-"))
        storage[idx] = row.copy()
        idx += 1

    idx -= 1
    for i in reversed(range(idx)):
        row = storage[i]
        print("-".join(row).center(size * 4 - 3, "-"))


if __name__ == "__main__":
    n = int(input())
    print_rangoli(n)
