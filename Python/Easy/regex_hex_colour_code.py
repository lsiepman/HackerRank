import re


if __name__ == "__main__":
    N = int(input())
    codes = []
    for _ in range(N):
        inp = input().strip()
        if inp.startswith("#"):
            continue
        res = re.findall(r"#[A-Fa-f0-9]{3,6}", inp)
        res_lst = list(res)
        if len(res_lst) == 0:
            continue
        else:
            codes.extend(res_lst)

    for i in codes:
        print(i)
