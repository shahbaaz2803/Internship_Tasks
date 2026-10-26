# Sherlock and the Valid String
# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

from collections import Counter

def isValid(s):
    freq = Counter(s).values()
    freq_count = Counter(freq)

    if len(freq_count) == 1:
        return "YES"

    if len(freq_count) == 2:
        (f1, c1), (f2, c2) = freq_count.items()

        if (f1 == 1 and c1 == 1) or (f2 == 1 and c2 == 1):
            return "YES"

        if abs(f1 - f2) == 1 and (c1 == 1 or c2 == 1):
            return "YES"

    return "NO"


if __name__ == '__main__':
    s = input().strip()
    print(isValid(s))
