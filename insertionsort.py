#insertionsort
arr =[1,4,5,3,2,1,9,5]
for i in range(len(arr)):
    second = arr[i]
    j =i-1
    while j>=0 and second<arr[j]:
        arr[j+1] = arr[j]
        j-=1
    arr[j+1] = second    