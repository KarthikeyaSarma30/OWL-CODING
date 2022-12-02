#Linear Search
#Complexity: best case-O(1);worst case-O(n)
def linearsearch(l,key):
    for i in range(len(l)):
        if l[i]==key :
            return i
    return "Not Found"





res=linearsearch([1,53,3,55,6],5)
print(res)


