def isPrime(n):
    if n < 2:
        return False
    elif n in [2, 3, 5, 7]:
        return True
    elif n % 2 == 0 or n % 3 ==0:
        return False
    else:
        r = 5
        while r * r <= n:
            if n % r == 0:
                return False
            r += 2
            if n % r == 0:
                return False
            r += 4
        return True


def nth_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    i = 23
    while len(primes) < n:
        for z in (filter(isPrime, [x for x in range(i,i + 20)])):
            primes.append(z)
        i += 10
    return primes[n-1]

print(nth_prime(10001))