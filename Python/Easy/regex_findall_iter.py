import re


if __name__ == "__main__":
    s = input()
    substrings = re.findall(
        r"(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])",
        s,
        re.IGNORECASE,
    )
    if substrings:
        for i in substrings:
            print(i)
    else:
        print(-1)
