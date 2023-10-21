from collections import defaultdict
from bs4 import BeautifulSoup


def fetch_attrs(s, attr_dct):
    soup = BeautifulSoup(s, "html.parser")
    result = soup.find_all()
    tags = [t.name for t in result]
    attributes = [t.attrs for t in result]

    for i, j in zip(tags, attributes):
        attr_dct[i].update(list(j.keys()))

    return attr_dct


def print_attrs(attrs_dict):
    sorted_keys = sorted(list(attrs_dict))

    for i in sorted_keys:
        print(f"{i}:{','.join(sorted(attrs_dict[i]))}")


if __name__ == "__main__":
    N = int(input())
    attrs = defaultdict(set)
    for _ in range(N):
        attrs = fetch_attrs(input(), attrs)

    print_attrs(attrs)
