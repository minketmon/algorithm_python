s = input()
ss = []
sum = 0

for i in range(len(s)):
    if s[i].isalpha(): #0 <= ord(s[i])-65 <=25: # 대문자
        ss.append(s[i])
    else: # 숫자
        sum += int(s[i])

ss.sort()
if sum!=0: ss.append(str(sum))
print(''.join(map(str, ss)))