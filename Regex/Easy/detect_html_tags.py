import re


def find_tags(d):
    tags = []
    for i in d:
        tags.extend(re.findall(r"<([a-z0-9]+)(\s|\>)", i))

    tags = sorted(list(set([i[0] for i in tags])))

    return ";".join(tags)


if __name__ == "__main__":
    N = int(input())
    data = []
    for i in range(N):
        data.append(input())
    print(find_tags(data))
