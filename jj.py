def solution(character, monsters):
    res = []
    m = []
    for monster in monsters:
        temp = list(map(str, monster.split()))
        m.append(temp[0])
        if fight(character, monster)[0] == "1":
            res.append(-1)
        else:
            res.append((int(temp[1]) / int(fight(character, monster)[1])))
    who = res.index(max(res))
    answer = m[who]
    return answerㅎ


def fight(character, monster):
    c = []
    m = []
    c = list(map(int, character.split()))
    temp = list(map(str, monster.split()))
    for i in range(1, 5):
        m.append(int(temp[i]))

    begin = c[0]
    count = 0
    while True:
        count += 1
        if c[1] - m[3] > 0:
            m[1] -= (c[1] - m[3])
        if m[1] <= 0:  # 몬스터사망
            return "0" + str(count)
        if m[2] - c[2] > 0:
            c[0] -= (m[2] - c[2])
        if c[0] <= 0:  # 플레이어사망
            return "1" + str(count)
        if c[0] > 0:
            c[0] = begin