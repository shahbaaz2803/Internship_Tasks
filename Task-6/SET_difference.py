# SET Difference
# https://www.hackerrank.com/challenges/py-set-difference-operation/problem

if __name__ == '__main__':
    n = int(input())
    english = set(map(int, input().split()))

    b = int(input())
    french = set(map(int, input().split()))

    only_english = english.difference(french)
    print(len(only_english))
