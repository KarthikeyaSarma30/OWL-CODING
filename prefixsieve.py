primes=[]
n=int(input())
for i in range(n+1):
    primes.append(1)
if n==0 or n==1:
    print(0)
for i in range(2,n+1):
    if primes[i]==True:
        for j in range(i*i,n+1,i):
            primes[j]=0
prefix=[0]*len(primes)
for i in range(2,len(primes)):
    prefix[i]=prefix[i-1]+primes[i]
print(prefix[n])
