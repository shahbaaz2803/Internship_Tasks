# Alphabet Rangoli
# https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def print_rangoli(size):
    import string
    alphabet = string.ascii_lowercase
    lines = []

    for i in range(size):
        row = [alphabet[size - 1 - j] for j in range(i + 1)]
        row = row[::-1] + row[-2::-1]
        line = "-".join(row)
        lines.append(line.center(4 * size - 3, "-"))

    return "\n".join(lines + lines[-2::-1])


if __name__ == '__main__':
    n = int(input())
    print(print_rangoli(n))
