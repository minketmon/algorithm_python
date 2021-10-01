s = input()
result = int(s[0])

for i in range(len(s)):
    if (i+1) >= len(s):
        break
    if result == 0 or result == 1 or int(s[i+1]) == 0 or int(s[i+1]) == 1:
        result += int(s[i+1])
    else:
        result *= int(s[i+1])

print(result)