def dsa_grill(ele):
    str1=''
    num=0
    for i in ele:
        if '0'<=i<= '9':
            num=num*10 + (ord(i)-ord('0'))  #ord() converts character to ASCII value and in (ord(i)-ord('0')) we substracting the ASCII value of i and 0 which will give us exact int value of i..eg. 
        else:
            str1 = str1 + i
    return num,str1

ele=(input("Enter a String :"))
print(dsa_grill(ele))


