def check_anagram(str1,str2):
    a=list(str1)
    b=list(str2)
    n1=len(a)
    n2=len(b)
    for i in range(n1):
        for j in range(n1-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    print("sorted",a)
    for i in range(n2):
        for j in range(n2-i-1):
            if b[j]>b[j+1]:
                b[j],b[j+1]=b[j+1],b[j]
    print("sorted",b)
    if a==b:
        return "Anagram"
    else:
        return "Not Anagram"
str1=input("Enter a string :")
str2=input("Enter a string :")
print(check_anagram(str1,str2))


