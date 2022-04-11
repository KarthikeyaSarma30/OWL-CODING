n=int(input())
l=list(map(int,input().split()))
for i in range(2**n):
    ans=[]
    for j in range(n):
        if i & 1<<j:
            ans.append(l[j])
    print(ans)
