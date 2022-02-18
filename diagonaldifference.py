def diagonalDifference(arr):
    # Write your code here
    d1 = sum([arr[x][x] for x in range(len(arr))])
    d2 = sum([arr[x][n - 1 - x] for x in range(len(arr))])

    return (abs(d1 - d2))

if __name__ == "__main__":

    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    result = diagonalDifference(arr)
    print(result)
