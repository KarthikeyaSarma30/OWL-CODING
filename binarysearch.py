#Binary Search(Sorted Array)
#Complexity: Best case-O(1);Worst Case-O(logn)

def binarysearch(l,key):
    low=0
    high=len(l)-1

    while low<=high:
        mid=(low+high)>>1
        if l[mid]==key:
            return mid
        elif l[mid]<key:
            low=mid+1
        else:
            high=mid-1
    return "Not Found"



res=binarysearch([1,4,5,6,7,9],7)
print(res)
