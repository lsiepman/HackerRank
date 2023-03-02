if __name__ == "__main__":
    K = int(input())
    rooms = list(map(int, input().split()))

    unique_rooms = set(rooms)

    total_value = sum(rooms)
    expected_value = sum(unique_rooms) * K

    print((expected_value - total_value) // (K - 1))
