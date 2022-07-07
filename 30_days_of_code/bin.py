import re


def solve(num):
    num_bin = bin(num)[2:]
    check = re.findall(r'[1]{1,}', num_bin)
    print(len(max(check)))


if __name__ == "__main__":
    solve(int(input()))