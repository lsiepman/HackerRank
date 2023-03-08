from itertools import combinations_with_replacement

if __name__ == "__main__":
    s, n = input().split()
    ans = list(combinations_with_replacement(sorted(s), int(n)))
    for i in ans:
        print("".join(i))
