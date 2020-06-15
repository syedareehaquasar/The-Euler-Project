def smallestMultiple(upto):
    num = upto
    c = 1
    for i in range(1, upto + 1):
        while num % i != 0:
            c += 1
            num *= c
    return num

print(smallestMultiple(10))