def wrapper(f):
    def fun(lst):
        l2 = []
        for i in lst:
            if len(i) == 11:
                l2.append(f"+91 {i[1:6]} {i[6:]}")
            elif len(i) == 10:
                l2.append(f"+91 {i[:5]} {i[5:]}")
            elif len(i) == 12:
                l2.append(f"+{i[0:2]} {i[2:7]} {i[7:]}")
            elif len(i) == 13:
                l2.append(f"{i[0:3]} {i[3:8]} {i[8:]}")

        f(l2)

    return fun


@wrapper
def sort_phone(lst):
    print(*sorted(lst), sep="\n")


if __name__ == "__main__":
    lst = [input() for _ in range(int(input()))]
    sort_phone(lst)
