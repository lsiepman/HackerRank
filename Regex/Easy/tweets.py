import re


def check_tweet(s):
    if re.search(r"hackerrank", s, re.IGNORECASE):
        return True
    else:
        return False


if __name__ == "__main__":
    N = int(input())
    num_tweets = []
    for i in range(N):
        num_tweets.append(check_tweet(input()))

    print(sum(num_tweets))
