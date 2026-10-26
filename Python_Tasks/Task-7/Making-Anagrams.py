# Making Anagrams
# https://www.hackerrank.com/challenges/making-anagrams/problem

def makingAnagrams(s1, s2):
    count = 0

    for ch in "abcdefghijklmnopqrstuvwxyz":
        count += abs(s1.count(ch) - s2.count(ch))

    return count


if __name__ == '__main__':
    s1 = input().strip()
    s2 = input().strip()

    print(makingAnagrams(s1, s2))
