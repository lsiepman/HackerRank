def count_occurences(word_us, data):
    word_uk = word_us[:-2] + "se"
    cnt = 0
    for sentence in data:
        cnt += sentence.count(word_uk)
        cnt += sentence.count(word_us)

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
