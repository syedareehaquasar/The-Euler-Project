from math import sqrt

def isPrime(n):
    if n <= 1:
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

def primefac(num):
    return [ans for ans in filter(isPrime, range(int(sqrt(num) + 1))) if num % ans == 0][-1:]

print(primefac(13195))