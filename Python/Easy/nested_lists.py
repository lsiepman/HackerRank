if __name__ == "__main__":
    names = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        names.append(name)
        scores.append(score)

    second_lowest = sorted(list(set(scores)))[1]

    print_names = []
    for idx, value in enumerate(scores):
        if value == second_lowest:
            print_names.append(names[idx])

    for i in sorted(print_names):
        print(i)
