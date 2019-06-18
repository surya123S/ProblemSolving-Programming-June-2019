#1. Function to check prime

def isPrime(num):
    flag = 1
    if(num==2):
        return "prime"
    else:
        for i in range(2, num):
            if(num%i == 0):
                flag = 0
                return "not prime"
        if(flag == 1):
            return "prime"
        
#2. Function to determine no of prime factors for a given number

def noofPrimeFactors(n):
    count = 0
    '''if(isPrime(n) == "prime"):
        return 1'''
    for i in range(2, n):
        if(isPrime(i) == "prime"  and n%i == 0):
            count += 1
    return count