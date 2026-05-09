#without size of the array
#def arraysum(a):
#    sum=0
#    for i in a:
#        sum=sum+i
#    return sum
#a=eval(input("Enter a Array:"))
#print(arraysum(a))

#with size of the array
def arraysum(n,a):
    sum=0
    for i in range(0,n):
        sum=sum+a[i]
    return sum
n=int(input("Enter list size:"))
a=eval(input("Enter a Array:"))
print(arraysum(n,a))

