def execute_commands(A, cmd, data):
    if "intersection_update" in cmd:
        A.intersection_update(data)
    elif "symmetric_difference_update" in cmd:
        A.symmetric_difference_update(data)
    elif "difference" in cmd:
        A.difference_update(data)
    elif "update" in cmd:
        A.update(data)

    return A


if __name__ == "__main__":
    n = int(input())
    A = set(map(int, input().split()))
    N = int(input())
    others = []
    for i in range(N):
        instruction, n_set = input().split()
        oth_set = set(map(int, input().split()))
        others.append((instruction, oth_set))

    for i, j in others:
        A = execute_commands(A, i, j)

    print(sum(A))
