#LCM of an array

def gcd(a,b):
    minimum=min(a,b)
    maximum=max(a,b)
    a=maximum
    b=minimum
    if b==0:
        return a
    else:
        return gcd(b,a%b)

l=list(map(int,input().split()))
ans=l[0]
for i in range(1,len(l)):
    ans=(l[i]*ans)/gcd(l[i],ans)

print(ans)
