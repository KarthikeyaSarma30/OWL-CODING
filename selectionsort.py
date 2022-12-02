#Selection sort
#Complexity -O(n^2)

def selectionsort(l):
    for i in range(len(l)):
        minind=i
        for j in range(i+1,len(l)):
            if l[j]<l[minind]:
                minind=j
        l[i],l[minind]=l[minind],l[i]


l=[22,11,4,77,45,67]
selectionsort(l)
print(l)
