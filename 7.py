def isPrime(n):
    if n < 2:
        return False
    elif n in [2, 3, 5, 7]:
        return True
    elif n % 2 == 0 or n % 3 == 0:
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


def primeUptoN(n):
    return [2] + list(filter(isPrime, range(1, n + 1, 2)))


def nth_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    i = 23
    while len(primes) < n:
        if isPrime(i):
            primes.append(i)
        i += 2
    return primes[n - 1]


def find_prime_num_poss(n):
    return len([2] + list(filter(isPrime, range(1, n + 1, 2))))


print(primeUptoN(13))
print(find_prime_num_poss(13))
print(nth_prime(10001))
print(nth_prime(6))
print(find_prime_num_poss(nth_prime(10001)))
print(find_prime_num_poss(104759))
