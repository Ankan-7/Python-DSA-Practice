#checking prime number in a range
def prime_range(a,b):
    pr=[]

    for i in range(a,b+1):
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                pr.append(i)
    return pr

a=int(int(input("Enter a starting range:")))
b=int(int(input("Enter a ending range:")))
print(prime_range(a,b))


