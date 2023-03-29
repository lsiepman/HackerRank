import re

if __name__ == "__main__":
    s = input().strip()
    k = input().strip()
    res = map(
        lambda x: (x.start(1), x.end(1) - 1), re.finditer(r"(?=(%s))" % k, s)
    )
    res_lst = list(res)

    if len(res_lst) > 0:
        for i in res_lst:
            print(i)
    else:
        print("(-1, -1)")
