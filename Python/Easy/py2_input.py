# While this challenge was meant for python 2, I'm implementing it in python 3
import seval

if __name__ == "__main__":
    # Solution 1 (HackerRank doesn't import seval)
    x, k = map(int, input().split())
    inp = input()
    temp = inp.replace("x", str(x))
    P = seval.safe_eval(temp)
    print(P == k)

    # Solution 2, which is unsafe, but accepted at HackerRank
    x, k = map(int, input().split())
    inp = input()
    temp = inp.replace("x", str(x))
    P = eval(temp)
    print(P == k)
