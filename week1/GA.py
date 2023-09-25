def fun(S):
    p = 0
    S = S.lower()
    for i in range(len(S)):
        if S[i] not in S[:i]:
            p += 1
    return p


def f(n):
    s = 0
    for i in range(2, n):
        if n % i == 0 and i % 2 == 1:
            s += 1
    return s


def q4():
    x = 1
    while True:
        if x % 5 == 0:
            break
        print(x, end=' ')
        x += 1

    return None

def q5():
    a = [1,2,3]
    try:
        print(a[1])
        print(a[3])
    except:
        print('error')

def gcd(m,n):
    # counter = 0
    (a,b) = (max(m,n),min(m,n))
    if a% b == 0:
        return b
    else:
        print('a')
        return gcd(b,a%b)

def special3Bad(L):
    try:
        if L[0] % L[1] == 0 and L[1] !=0:
            if L[0] / (L[1] **2 -L[2]) == 0:
                return True
        return False
    except ZeroDivisionError:
        print('ZeroDivisionError')
    except:
        print('some Other error')
    else:
        print('No exception')

def isSymmetricBad(L):
    try:
        while len(L) > 0:
            if L.pop(0) != L.pop(-1):
                return False
        return True
    except IndexError:
        print("index Error")
    except:
        print('some other exception')

L = [2,4,6]
isSymmetricBad(L)