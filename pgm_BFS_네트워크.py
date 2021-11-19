def solution(n, computers):
    answer = 0
    visited = [False] * n

    for i in range(n):
        if visited[i] == False:
            BFS(n, computers, i, visited)
            answer += 1
    return answer


def BFS(n, computers, start, visited):
    visited[start] = True
    queue = []
    queue.append(start)
    while len(queue) != 0:
        visited[start] = True
        start = queue.pop()
        for i in range(n):
            if start != i and computers[start][i] == 1 and visited[i] == False:
                BFS(n, computers, i, visited)