a=int(input())
b=int(input())
c=1

while c:
    c=a&b
    a=a^b
    b=c<<1

print(a)





    
