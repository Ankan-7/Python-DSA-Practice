n=int(input("Enter a Number :"))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print(f"{n} is not a Prime Number.")
            break
    else:
        print(f"{n} is a Prime Number.")
else:
    print(f"{n} is not a Prime Number.")
