if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        inp = input().strip()
        try:
            float(inp)
            if inp != "0":
                print(True)
            else:
                print(False)
        except Exception:
            print(False)
