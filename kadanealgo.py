#Kadane's Algorithm(Maximum SubArray Sum)

def kadane(l):
    max_till_now=0 #for updating max value based on max_go 
    max_go=0 #should be >=0

    for i in range(len(l)):
        max_go=max_go+l[i]
        if max_go<0:
            max_go=0
        max_till_now=max(max_till_now,max_go)
    return max_till_now


print(kadane([-2,-3,4,-1,-2,5,-3])) #6(4,-1,-2,5)
    
