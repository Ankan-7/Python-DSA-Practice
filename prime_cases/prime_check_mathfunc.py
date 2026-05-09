# Simple program to check if a number is prime using math module
import math
def prime_check(num):
    if num > 1:
        # Check for factors
        # Instead of math.sqrt(num)
        #for i in range(2, int(num**0.5) + 1):
        for i in range(2, int(math.sqrt(num)) + 1):
            if (num % i) == 0:
                return(f"{num} is not a prime number.")
        else:
            return(f"{num} is a prime number.")
    else:
        return(f"{num} is not a prime number.")

num = int(input("Enter a number: "))
print(prime_check(num))