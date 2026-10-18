# Set Intersection
# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem


if __name__ == '__main__':
    n = int(input())
    english = set(map(int, input().split()))

    b = int(input())
    french = set(map(int, input().split()))

    common = english.intersection(french)
    print(len(common))
