n, k = map(int, input().split())
result = 0

#1
while True:
    if n==1: break
    if n%k==0:
        n/=k
        result+=1
    else:
        n-=1
        result+=1
    print("n", n)
print(result)

#2
while True:
    target = (n//k) * k
    result += (n-target)
    n = target

    if n<k: break

    result+=1
    n//=k
result += (n-1)
print(result)