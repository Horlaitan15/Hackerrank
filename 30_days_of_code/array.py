def solve(lst):
    print(*[i for i in reversed(lst)])


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    solve(arr)
