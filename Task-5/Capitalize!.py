# Capitalize!
# https://www.hackerrank.com/challenges/capitalize/problem

s = input()
result = []

for word in s.split(' '):
    if word and word[0].isalpha():
        word = word[0].upper() + word[1:]
    result.append(word)

print(' '.join(result))
