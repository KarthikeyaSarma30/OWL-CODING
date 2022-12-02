#Quick Sort(Divide and conquer approach)
#Complexity -O(n*logn)

def partition(l,low,high):
    pivot=l[high]
    i=low
    j=high

    while i<j:
        while i<high and l[low]<pivot:
            i+=1
        while j>low and l[high]>=pivot:
            j-=1

        if i<j:
            l[i],l[j]=l[j],l[i]
    if l[i]>pivot:
        l[high],l[j]=l[j],l[high]
    return j

def quicksort(l,low,high):
    if low<high:
        j=partition(l,low,high)
        quicksort(l,low,j-1)
        quicksort(l,j+1,high)

l=[1,2,77,43,54,65]
quicksort(l,0,len(l)-1)
print(l)
