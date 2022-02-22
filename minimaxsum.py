def arrayaddition(arr):
    arr.sort()
    all = sum(arr)
    sumoffirst = all -arr[0]
    sumoflast = all - arr[len(arr) -1]
    print(sumoflast,sumoffirst)


if __name__ == "__main__":
    arr = list(map(int,input().split()))
    arrayaddition(arr)
