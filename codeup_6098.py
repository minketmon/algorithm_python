arr = [list(map(int, input().split())) for _ in range(10)]
cur_x, cur_y = 1,1

while cur_x!=9 and cur_y!=9:
    if arr[cur_x][cur_y]==2:
        arr[cur_x][cur_y]=9
        break
    arr[cur_x][cur_y]=9
    if arr[cur_x][cur_y+1] != 1: #통로거나 먹이거나
        cur_y+=1
    else: #장애물
        cur_x+=1

for i in range(len(arr)):
    print(' '.join(map(str,arr[i])))