# 최대공약수

def uclid(a, b):
    if a%b == 0:
        return b
    return uclid(b, a%b)

print(uclid(192,162))