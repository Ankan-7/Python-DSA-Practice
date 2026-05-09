def miss_array(arr):
    max=arr[0]
    min=arr[0]
    miss=[]
    for i in arr:
        if i>max:
            max=i
        elif i<min:
            min=i
    for i in range(min,max+1):
        if i not in arr:
            miss.append(i)
    return miss

arr=eval(input("Enter an array:"))
print(miss_array(arr))