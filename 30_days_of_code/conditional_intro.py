def solve(n):
    return "Weird" if n % 2 != 0 or n in range(6, 21) else "Not Weird"


if __name__ == '__main__':
    N = int(input().strip())
    print(solve(N))
