def linear_search(arr,target):
    n=len(arr)
    for i in range(n):
        if arr[i]==target:
            return "Found"
        
    return "Item doesnt exist"
arr=eval(input("Enter a Collection:"))
target=eval(input("Enter the Target element:") )
print(linear_search(arr,target))