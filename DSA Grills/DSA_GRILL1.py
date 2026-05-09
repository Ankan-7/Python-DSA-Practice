def dsa_grill(arr,sum_arr):
    n1=len(arr)
    result = []
    for i in range(n1-1):
        s=arr[i]+arr[i+1]
        if s in sum_arr:
            result.append(arr[i])
            result.append(s)
            new=i
    result.append(arr[new+1])
    return result

arr=eval(input("Enter an Array :"))
sum_arr=eval(input("Enter an Sum Array :"))
print(dsa_grill(arr,sum_arr))

''' INPUT ARRAY and a SUM ARRAY will be given..check if the thre sum if two adjacent element in the input array is in the sum array or not..if it is then return a new array with the input elemnt with the sum element in between... 
eg. Enter an Array :[1,2,3,4,5]
Enter an Sum Array :[3,5,12]
[1, 3, 2, 5, 3] '''


