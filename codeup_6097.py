h, w = map(int, input().split())
n = int(input())
lis = [list(map(int, input().split())) for _ in range(n)]

arr = [[0 for i in range(w)] for j in range(h)]

for i in range(n):
    l, d, x, y = lis[i]
    x-=1
    y-=1
    if d==0:
        for j in range(y, y+l):
            if j > w: break
            arr[x][j] = 1
    elif d==1:
        for j in range(x, x+l):
            if j > h: break
            arr[j][y] = 1

for i in range(len(arr)):
    print(' '.join(map(str, arr[i])))