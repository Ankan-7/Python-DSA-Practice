""""
Medium : MSS With Swaps
Given an array a of length n and an integer k. You must perform the following operation exactly k times:
choose two indices i, j and swap**(ai, aj).**
Find the maximum possible MSS (maximum subarray sum) after performing the above operation exactly
k times.
Note:
Swapping the same pair again is allowed but useless (a double-swap cancels out). Therefore,
performing exactly k swaps is equivalent to at most k useful swaps.
Input Format
The first line contains an integer, n, denoting the size of array
The next line contains an integer, k, denoting the number of swaps.
Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer describing a[i].
Constraints
2 <= n <= 500
0 <= k <= n
-1000 <= a[i] <= 1000
Sample Test Cases
Case 1
Input:
3
 1
 1
 -5
 2
Output:
3
Explanation:
By swapping 1 and -5, we get a maximum subarray sum equal to 1 + 2 = 3.
Case 2
Input:
3
 0
 5
 -1
 5
Output:
9
Explanation:
The maximum array sum is equal to the sum of the entire array 5 - 1 + 5 = 9, and it's not possible to
achieve a greater sum.
Case 3
Input:
3
0
1
-5
2
Output:
2
Explanation:
The maximum subarray sum is the sum of [2] which is equal to 2.
"""
def max_num_subarr(a):
    p,c=a[0],a[0]
    for i in range(1,len(a)):
        p=max(a[i],p+a[i])
        c=max(c,p)
    return c
def mss_swap(a,k):
    b=max_num_subarr(a)
    if k==0:
        return b
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            a[i],a[j]=a[j],a[i]
            b=max(b,mss_swap(a,k-1))
            a[i],a[j]=a[j],a[i]
    return b
n=int(input("Enter the length of the array :"))
k=int(input("Enter the number of time the operation will execute :"))
a=[]
for i in range(n):
    a.append(int(input("Enter a Number:")))
print(mss_swap(a,k))
    







