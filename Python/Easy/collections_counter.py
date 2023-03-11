from collections import Counter

if __name__ == "__main__":
    x = int(input())
    sizes_avail = list(map(int, input().split()))
    sizes_avail = Counter(sizes_avail)
    n = int(input())
    money = []
    sizes = []
    for _ in range(n):
        size, price = map(int, input().split())
        if sizes_avail[size] > 0:
            money.append(price)
            sizes.append(size)
            sizes_avail[size] -= 1

    print(sum(money))
