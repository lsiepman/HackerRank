if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())
    nums = sorted(list(set(arr)))
    print(nums[-2])
