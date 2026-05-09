# Simple program to check if a number is prime
def prime_check(num):
    if num > 1:
        # Check for factors
        for i in range(2, num):
            if (num % i) == 0:
                return(f"{num} is not a prime number.")
        else:
            return(f"{num} is a prime number.")
    else:
        return(f"{num} is not a prime number.")

num = int(input("Enter a number: "))
print(prime_check(num))