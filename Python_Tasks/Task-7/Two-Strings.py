# Two Strings
# https://www.hackerrank.com/challenges/two-strings/problem

def twoStrings(s1, s2):
    if set(s1).intersection(set(s2)):
        return "YES"
    return "NO"


if __name__ == '__main__':
    t = int(input().strip())

    for _ in range(t):
        s1 = input().strip()
        s2 = input().strip()

        result = twoStrings(s1, s2)
        print(result)
