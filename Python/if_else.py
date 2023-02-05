if __name__ == "__main__":
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    else:
        if n in range(2, 5 + 1):
            print("Not Weird")
        elif n in range(6, 20 + 1):
            print("Weird")
        elif n > 20:
            print("Not Weird")
