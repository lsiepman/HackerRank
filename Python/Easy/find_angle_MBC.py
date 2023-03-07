import math

if __name__ == "__main__":
    AB = int(input())
    BC = int(input())
    MBC = math.degrees(math.atan(AB / BC))  # MBC = MCB = ACB
    print(f"{round(MBC)}{chr(176)}")
