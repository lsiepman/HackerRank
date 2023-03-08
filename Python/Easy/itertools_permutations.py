from itertools import permutations

if __name__ == "__main__":
    s, n = input().split()
    ans = list(permutations(list(s), int(n)))
    for i in sorted(ans):
        print("".join(i))
