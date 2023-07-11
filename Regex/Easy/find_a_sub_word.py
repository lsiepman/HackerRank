import re


def count_occurences(query, data):
    occs = []
    for i in data:
        occs.extend(re.findall(r"\w(" + query + r")\w", i))

    print(len(occs))


if __name__ == "__main__":
    n = int(input())
    data_n = []
    for idx in range(n):
        data_n.append(input())

    q = int(input())
    data_q = []
    for idx in range(q):
        data_q.append(input())

    for query in data_q:
        count_occurences(query, data_n)
