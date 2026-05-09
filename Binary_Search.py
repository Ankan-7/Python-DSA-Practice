def binary_search(arr,target):
    arr.sort()
    low,high=0,len(arr)-1
    while low<=high:
        mid=(high+low)//2
        if arr[mid]==target:
            return "Found"
        elif arr[mid]>target:
            high=mid-1
        else:
            low=mid+1
    return "Element doesnt exist"
arr=eval(input("Enter a Collection:"))
target=eval(input("Enter the Target element:") )
print(binary_search(arr,target))
