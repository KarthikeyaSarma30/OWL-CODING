l=list(map(int,input().split()))
prefix=[0]*len(l)
for i in range(len(l)):
    prefix[i]=prefix[i-1]+l[i]
print(prefix)
i1=int(input())
i2=int(input())
print(prefix[i2]-prefix[i1-1])
