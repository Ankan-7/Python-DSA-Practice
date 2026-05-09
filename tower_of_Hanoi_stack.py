def hanoi_tower(n,source,aux,target):
    if n==1:
        print(source,"->",target)
        return
    hanoi_tower(n-1,source,target,aux)
    print(source,"->",target)
    hanoi_tower(n-1,aux,source,target)
hanoi_tower(3,'A','B','C')
