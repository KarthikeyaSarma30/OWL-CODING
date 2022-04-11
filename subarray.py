n=int(input())
l=list(map(int,input().split()))
ans=[]
for i in range(len(l)+1):
    for j in range(i):
        ans.append(l[j:i])
print(ans)
