n = int(input())
move = input().split()
cur_x, cur_y = 0, 0
print(move)
# 상 하 좌 우
x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]
control = ['U', 'D', 'L', 'R']
for i in move:
    for j in range(len(control)):
        if i==control[j]:
            temp_x = cur_x + x[j]
            temp_y = cur_y + y[j]
    if temp_x < 0 or temp_y < 0 or temp_y >= n or temp_x >= n:
        continue
    cur_x, cur_y = temp_x, temp_y
    print(cur_x, cur_y)
cur_x+=1
cur_y+=1
print(cur_x, cur_y)