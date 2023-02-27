if __name__ == "__main__":
    n_students = int(input())
    n_roll_nums = set(map(int, input().split()))
    b_subs = int(input())
    b_roll_nums = set(map(int, input().split()))

    print(len(n_roll_nums.intersection(b_roll_nums)))
