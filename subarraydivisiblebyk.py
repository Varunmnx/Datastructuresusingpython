A=[1,2,3,4,5]
prefix_sum=0
K=6
sums = {0: 1}
answer = 0
for num in A:
    prefix_sum += num
    key = prefix_sum%K
    if key in sums:
        answer += sums[key]
        sums[key] += 1
        continue
    sums[key] = 1
print(answer)