#  finding all the factors
def factor(n):
    factors = list()
    for i in range(1,n+1):
        if n%i == 0:
            factors.append(i)
    
    return factors

# checking if factors list contians only two factors 1 and n
def prime(n):
    return (factor(n) == [1,n])



# to find prime, checking if n has a factor other than 1 and n
def prime1(n):
    prime = True
    for i in range(2,n):
        if n % i==0:
            prime = False
            break
    return prime

def prime1_1(n):
    (prime,i) = (True,2)
    while (prime and (i<n)):
        if n%i == 0:
            prime = False
        i = i + 1
    return prime

# optimised prime checking using sqrt(n)
import math
def prime2(n):
    prime = True
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            prime = False
            break
    return prime



# checking all primes upto n
def primeupto(n):
    primes = list()
    for i in range(1,n+1):
        if prime(i):
            primes.append(i)
    return primes



# finding first m primes
def firstprimes(m):
    (count,i, primes) = (0,1,list())
    while count<=m:
        if prime1(i):
            primes.append(i)
            count +=1
        i = i+1
    return primes

def firstprimes2(m):
    (count,i, primes) = (0,1,list())
    while count<=m:
        if prime2(i):
            primes.append(i)
            count +=1
        i = i+1
    return primes

# checking the difference bw two prime numbers
def primediff(n):
    lastPrime = 2
    pd = dict()
    for i in range(3,n+1):
        if prime2(i):
            # print(f'difference between {i} and {lastPrime} is {i-lastPrime}')
            diff = i-lastPrime
            if diff not in pd.keys():
                pd[diff] = 0
            pd[diff] = pd[diff] +1
            lastPrime = i
    return pd

# counting prime between m and n
def countprime(m,n):
    counter = 0
    for i in range(m,n+1):
        if prime2(i):
            counter+=1
        return counter