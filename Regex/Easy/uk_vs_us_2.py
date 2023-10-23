import re


def count_occurences(word_uk, data):
    word_us = re.sub(r"our", "or", word_uk)
    cnt = 0
    for sentence in data:
        cnt += len(re.findall(word_uk + r"\b", sentence))
        cnt += len(re.findall(word_us + r"\b", sentence))

    print(cnt)


if __name__ == "__main__":
    N = int(input())
    data = []
    for _ in range(N):
        data.append(input())

    tests = []
    T = int(input())
    for _ in range(T):
        tests.append(input())

    for item in tests:
        count_occurences(item, data)
