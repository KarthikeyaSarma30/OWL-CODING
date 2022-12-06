#Fibonacci Series

def fibprint(n):
    a,b=0,1

    print(a,b,end=" ")
    term=3
    
    while term<=n:
        c=a+b
        print(c,end=" ")
        a=b
        b=c
        term+=1
    return c #nth number in Fibonacci series
print(fibprint(5)) #3
print(fibprint(60)) #956722026041
