# Anagram
# https://www.hackerrank.com/challenges/anagram/problem

from collections import Counter

def anagram(s):
    if len(s) % 2 != 0:
        return -1

    half = len(s) // 2
    first = Counter(s[:half])
    second = Counter(s[half:])

    changes = 0

    for ch in first:
        if first[ch] > second[ch]:
            changes += first[ch] - second[ch]

    return changes
