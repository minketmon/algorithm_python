def solution(n, computers):
    answer = 0
    visited = [False] * n

    for i in range(n):
        if visited[i] == False:
            DFS(n, computers, i, visited)
            answer += 1
    return answer


def DFS(n, computers, start, visited):
    visited[start] = True

    for i in range(n):
        if start != i and computers[start][i] == 1 and visited[i] == False:
            DFS(n, computers, i, visited)