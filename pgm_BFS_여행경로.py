def solution(tickets):
    answer = []
    tickets.sort(reverse=True)
    d = dict()
    for start, arrive in tickets:
        if start not in d:
            d[start] = [arrive]
        else:
            d[start].append(arrive)

    stack = ['ICN']
    while stack:
        top = stack[-1]
        if top not in d or len(d[top]) == 0:
            answer.append(stack.pop())
        else:
            stack.append(d[top].pop())
    answer.reverse()
    return answer



# def solution(tickets):
#     global answer
#     answer = []
#     visited = [False] * len(tickets)
#
#     route(tickets, "ICN", visited)
#     return answer
#
#
# def route(tickets, start, visited):
#     answer.append(start)
#     case = []
#     for ticket in tickets:
#         if ticket[0] == start and visited[tickets.index(ticket)] == False:
#             print(1, ticket)
#             case.append(ticket)
#     print(3)
#     case.sort(key=lambda x: x[1])
#     visited[tickets.index(case[0])] = True
#     route(tickets, case[0][1], visited)