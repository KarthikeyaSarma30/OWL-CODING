#Sieve of Eratosthenes
n=int(input())
primes=[]
for i in range(n+1):
    primes.append(True)
if n==0 or n==1:
    print(0)
for i in range(2,int(n**0.5)+1):
    if primes[i]:
        for j in range(i*i,n+1,i):
            primes[j]=False

for i in range(2,n):
    if primes[i]:
        print(i)

