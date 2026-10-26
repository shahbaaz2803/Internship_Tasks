# Pangrams
# https://www.hackerrank.com/challenges/pangrams/problem


def pangrams(s):
    s = s.lower()
    letters = set()

    for ch in s:
        if ch.isalpha():
            letters.add(ch)

    if len(letters) == 26:
        return "pangram"
    else:
        return "not pangram"


s = input()
print(pangrams(s))
