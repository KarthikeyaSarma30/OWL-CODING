#Binary Search(Sorted Array)
#Complexity: Best case-O(1);Worst Case-O(logn)

def binarysearchrecursive(l,low,high,key):
    if low<=high:
        mid=(low+high)>>1

        if l[mid]==key:
            return mid
        elif l[mid]<key:
            return binarysearchrecursive(l,mid+1,high,key)
        else:
            return binarysearchrecursive(l,low,mid-1,key)
    return "Not Found"

l=[1,3,5,7,8,9]
res=binarysearchrecursive(l,0,len(l)-1,10)
print(res)
