n = int(input())

arr = "1"
res = ""

for i in range(n-1):
    j = 0
    while j < len(arr):
        cur = arr[j]
        count = 1
        while j+1 < len(arr) and cur == arr[j+1]:
            count += 1
            j +=1
        res += cur + str(count)
        j += 1
    if i+1 == n-1: print(res)
    arr = res
    res = ""
