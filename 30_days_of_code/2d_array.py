#!/bin/python3

def solve(arr):
    # hour = []
    # for i in range(4):
    #     for j in range(4):
    #         inner = []
    #         p = arr[i][j: j + 3]
    #         m = arr[i + 1][j + 1: j + 2]
    #         n = arr[i + 2][j: j + 3]
    #         inner.append(p)
    #         inner.append(m)
    #         inner.append(n)
    #         hour.append(inner)
    #
    # glasses = [list(map(sum, lst)) for lst in hour]
    # print(max(list(map(sum, glasses))))

    glass = [[arr[i][j: j + 3], arr[i + 1][j + 1: j + 2], arr[i + 2][j: j + 3]] for i in range(4) for j in range(4)]
    print(max(list(map(sum, [list(map(sum, lst)) for lst in glass]))))



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    solve(arr)
