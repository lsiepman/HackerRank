if __name__ == "__main__":
    m = int(input())
    m_str = map(int, input().split())
    n = int(input())
    n_str = map(int, input().split())

    diff = set(m_str).symmetric_difference(set(n_str))
    diff = sorted(list(diff))
    for i in diff:
        print(i)
