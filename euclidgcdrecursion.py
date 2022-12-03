#Euclid algorithm(GCD of two numbers using recursion)
def gcd(a,b):
    minimum=min(a,b)
    maximum=max(a,b)
    a=maximum
    b=minimum
    if b==0:
        return a
    else:
        return gcd(b,a%b)

print(gcd(48,18))#6
