#  returning the GCD directly a
def gcd1(n,m):
    for i in range(1,min(m,n)+1):
        if m %i== 0 and n%i == 0:
            gcd = i

    return gcd

#  storing all the factors in a list then returning the last(greatest) factor from the list
def gcd2(n,m):
    gcd = list()
    for i in range(1,min(m,n)+1):
        if m %i== 0 and n%i == 0:
            gcd.append(i)

    return gcd[-1]


def gcd3(n,m):
    '''
        if d divides m and n
        then m = ad, n = bd
        m-n = ad-bd =>(a-b)d
        so if d divides m and n => d also divides m-n
    '''
    (a,b) = (max(m,n),min(m,n))
    if a%b == 0:
        return b
    return gcd3(b,a-b)


'''
    if n does not divide m,
    then m = qn + r
    if d divides both m and n,then
    m = ad, and n = bd
    ad = q(bd) + r
    r must be of the form cd
    ad = q(bd) + cd

    Euclid's algo
    if n divides m, then gcd(n,m) = n
    otherwise compute gcd(n,m mod n)
'''
def gcd4(n,m):
    (a,b) = (max(n,m),min(n,m))
    if a%b == 0:
        return b
    gcd4(b,a%b)




n = 99
m = 999
print(gcd3(m,n))

