# Separate the Numbers
# https://www.hackerrank.com/challenges/separate-the-numbers/problem

def separateNumbers(s):
    for i in range(1, len(s) // 2 + 1):
        first = s[:i]

        if first.startswith('0'):
            continue

        current = int(first)
        built = first

        while len(built) < len(s):
            current += 1
            built += str(current)

        if built == s:
            print("YES", first)
            return

    print("NO")


if __name__ == '__main__':
    q = int(input().strip())

    for _ in range(q):
        s = input().strip()
        separateNumbers(s)
