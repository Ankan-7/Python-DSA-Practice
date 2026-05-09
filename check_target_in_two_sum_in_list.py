def check_twosum(l1,target):
    n=len(l1)
    for i in range(n):
        for j in range(i+1,n):
            if l1[i]+l1[j]==target:
                print(l1[i],l1[j])
    return -1
l1=[3,5,7,2]
target=9
print(check_twosum(l1,target))
    
