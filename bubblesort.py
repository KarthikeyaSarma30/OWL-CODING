#Bubble sort(main operation-swap)
#complexity -O(n^2)

def bubblesort(l):

    for i in range(len(l)-1):
        for j in range(len(l)-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]


l=[11,7,4,3,55,77,23]
bubblesort(l)
print(l)
