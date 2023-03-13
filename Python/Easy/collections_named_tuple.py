from collections import namedtuple

if __name__ == "__main__":
    n = int(input())
    colnames = input().split()
    Student = namedtuple("Student", colnames)
    marks = []
    for _ in range(n):
        temp = Student._make(input().split())
        marks.append(int(temp.MARKS))

    print(sum(marks) / len(marks))
