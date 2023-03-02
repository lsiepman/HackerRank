if __name__ == "__main__":
    A = set(map(int, input().split()))
    n = int(input())
    ans = []
    for _ in range(n):
        temp = set(map(int, input().split()))
        ans.append(A.issuperset(temp) and A != temp)

    print(all(ans))
