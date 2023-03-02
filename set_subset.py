if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        num_A = int(input())
        A = set(map(int, input().split()))
        num_B = int(input())
        B = set(map(int, input().split()))
        print(A.issubset(B))
