if __name__ == "__main__":
    inp = [input() for _ in range(4)]
    a, b, c, d = map(int, inp)
    ans = a**b + c**d
    print(ans)
