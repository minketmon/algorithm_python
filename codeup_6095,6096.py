arr = [list(map(int, input().split())) for _ in range (19)]
n = int(input())
reverse = [list(map(int, input().split())) for _ in range(n)]

for i in range(len(reverse)):
    x, y = reverse[i]
    x-=1
    y-=1
    for j in range(19):
        if arr[x][j]==1: arr[x][j]=0
        elif arr[x][j]==0: arr[x][j]=1
    for j in range(19):
        if arr[j][y]==1: arr[j][y]=0
        elif arr[j][y]==0: arr[j][y]=1

for i in range(len(arr)):
    print(' '.join(map(str, arr[i])))

# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
#
# badook = [[0 for i in range(19)] for j in range(19)]
#
# for i in range(len(arr)):
#     x, y = arr[i]

#     badook[x-1][y-1] = 1
#
# for i in range(len(badook)):
#     print(" ".join(map(str, badook[i])))