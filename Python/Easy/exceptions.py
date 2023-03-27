if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        try:
            a, b = map(int, input().split())
            print(a // b)
        except Exception as e:
            print(f"Error Code: {e}")
