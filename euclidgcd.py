
def gcd(a,b):
    minimum=min(a,b)
    maximum=max(a,b)
    a=maximum
    b=minimum
    while b:
        temp=a
        a=b
        b=temp%b
    return a
print(gcd(48,18))
        
        
