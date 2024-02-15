def binary_search(res, target):

    res.sort()
    print(res)
    print("target=",target)
    high=len(res)-1
    low=0
    mid=0
    while low<=high:
        mid= (high+low)//2
        if res[mid]<target:
            low=mid+1
        elif res[mid]>target:
            high=mid-1
        else:
            return "index=",mid
    return -1

target=10
res=[2,3,7,5,6,10,8,1]
answer=binary_search(res,target)
print(answer)