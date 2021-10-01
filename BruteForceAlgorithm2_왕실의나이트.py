n = input()
x, y = ord(n[0])-97, int(n[1])-1
x_vec = [2, 2, -2, -2, 1, -1, 1, -1]
y_vec = [1, -1, -1, 1, -2, -2, 2, 2]
count = 0

for i in range(8):
    temp_x = x+x_vec[i]
    temp_y = y+y_vec[i]
    if temp_x < 0 or temp_y < 0 or temp_x > 7 or temp_y > 7:
        continue
    count+=1
print(count)