from collections import deque
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
n, m = map(int, input().split())
graph = []
queue = deque()
for i in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
count = 1
def bfs(x, y):
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<=-1 or ny>=m:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    graph[nx][ny]= graph[x][y]+1
    return graph[n-1][m-1]


print(bfs(0,0))
