def solution(begin, target, words):
    answer = 0
    words.insert(0, begin)
    visited = [False] * len(words)
    if target in words:
        answer = BFS(begin, target, words, visited)
    return answer


def BFS(begin, target, words, visited):
    ans = 0
    visited[words.index(begin)] = True
    queue = []
    queue.append(begin)
    while len(queue) != 0:
        temp = queue.pop()
        if temp==target:
            return ans
        else:
            for word in words:
                if compare(temp, word) and visited[words.index(word)] == False:
                    queue.append(word)
                    visited[words.index(word)] = True
                    print(temp, word)
                    print(visited)
            ans += 1

def compare(first, second):
    cnt = 0
    for i in range(len(first)):
        if first[i] == second[i]:
            cnt += 1
    if cnt == len(first) - 1:
        return True
    else:
        return False