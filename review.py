# Enter your code here. Read input from STDIN. Print output to STDOUT

def solve(s):
    # List coming lists append all even and odd alphabet.
    even = []
    odd = []
    for i, j in enumerate(s):
        if i % 2 == 0:
            even.append(j)
        else:
            odd.append(j)

    print(''.join(even), ''.join(odd))


if __name__ == "__main__":
    for _ in range(int(input())):
        s = input().rstrip()
        solve(s)

