
def primes(n):
    res = []
    for i in range(n):
        if is_prime(i):
            res.append(i)

    return res


def is_prime(n):
    if (n == 1):
        return False
    elif (n == 2):
        return True
    else:
        for x in range(2, n):
            if(n % x == 0):
                return False
        return True
