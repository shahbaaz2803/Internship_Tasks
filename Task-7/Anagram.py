# Anagram
# https://www.hackerrank.com/challenges/anagram/problem

def anagram(s):
    if len(s) % 2 != 0:
        return -1

    half = len(s) // 2
    first = s[:half]
    second = s[half:]

    for ch in second:
        first = first.replace(ch, "", 1)

    return len(first)
