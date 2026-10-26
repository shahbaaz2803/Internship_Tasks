# String Construction
# https://www.hackerrank.com/challenges/string-construction/problem

def stringConstruction(s):
    return len(set(s))


if __name__ == '__main__':
    n = int(input().strip())

    for _ in range(n):
        s = input().strip()
        print(stringConstruction(s))
