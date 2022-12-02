#Merge Sort(Divide and Conquer Approach)
#Complexity -O(n*logn)

def mergesort(l):
    if(len(l)>1):
        left_l=l[:len(l)//2]
        right_l=l[len(l)//2:]

        mergesort(left_l)
        mergesort(right_l)

        #Merging Process
        i=0 #left subarray idx
        j=0 #right subarray idx
        k=0 #merged arrray idx

        while i<len(left_l) and j<len(right_l):
            if left_l[i]<right_l[j]:
                l[k]=left_l[i]
                i+=1
                k+=1
            else:
                l[k]=right_l[j]
                j+=1
                k+=1
        while i<len(left_l):
            l[k]=left_l[i]
            i+=1
            k+=1
        while j<len(right_l):
            l[k]=right_l[j]
            j+=1
            k+=1


l=[55,33,22,75,4,9,10]
mergesort(l)
print(l)
