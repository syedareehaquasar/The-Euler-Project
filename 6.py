def sumSqr(t: int) -> int:
    return sum([x ** 2 for x in range(t + 1)])

def sqrSum(t : int) -> int:
    return sum([x for x in range(t + 1)]) ** 2

def sumSquareDiff(a : int, b : int) -> int:
    return a - b

print(sumSquareDiff(sqrSum(100), sumSqr(100)))
