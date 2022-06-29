def solve(n):
    multiples = [f"{n} x {i} = {n * i}" for i in range(1, 11)]
    print(*multiples, sep="\n")


if __name__ == '__main__':
    n = int(input().strip())
    solve(n)
