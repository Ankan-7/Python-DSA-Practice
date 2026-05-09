#checking prime number in a range and storing it in a list and then finding all the possible combinations for all the elements in prime list.
def prime_range_combo(a,b):
    pr=[]
    com=[]
    z=''

    for i in range(a,b+1):
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                pr.append(i)
    #
    for i in pr:
        for j in pr:
            m=str(i)
            n=str(j)
            z=m+n
            com.append(z)
    return com


a=int(int(input("Enter a starting range:")))
b=int(int(input("Enter a ending range:")))
print(prime_range_combo(a,b))


