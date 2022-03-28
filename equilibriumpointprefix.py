N=int(input())
A=list(map(int,input().split()))
s=sum(A)
prefix=[0]*N
if len(A)==1:
    print(1)
for i in range(N):
    prefix[i]=prefix[i-1]+A[i]
for i in range(1,N-1):
    if prefix[i-1]==s-prefix[i]:
        print(i+1)
        break
else:
    print(-1)
