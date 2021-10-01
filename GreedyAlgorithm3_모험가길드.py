n = int(input())
guild = list(map(int, input().split()))
result = 0
count = 0
guild.sort()

for i in guild:
    count+=1
    if count >= i:
        result +=1
        count = 0
print(result)

# 틀린 내 풀이
# for i in range(len(guild)):
#     if i>=len(guild): break
#     if i+guild[i]>=len(guild): break
#     guild = guild[guild[i]:]
#     count+=1
#     i+=guild[i]
#
# print(count)