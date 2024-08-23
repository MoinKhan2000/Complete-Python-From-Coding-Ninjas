def isPrime(n):
    prime = True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Normal way to print prime numbers from  2 to N 
"""def primeFrom2ToN(n):
    for k in range(2, n + 1):
        prime = True
        for l in range(2, k):
            if k % l == 0:
                prime = False
        if prime:
            print(k, end=", ")

primeFrom2ToN(10)"""


# Legend Way is this
def primeFrom2ToN(n):
    for k in range(2, n+1):
        if(isPrime(k)):
            print(k, end=", ")

primeFrom2ToN(10)


