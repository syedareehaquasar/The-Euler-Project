def is_palindrome(x):
    return str(x) == str(x)[::-1]

def palindromic_product(digits):
    for i in reversed(range(10 ** digits)):
        for j in reversed(range(i)):
            if is_palindrome(i * j):
                return str(i * j) + " = " + str(i) + " X " + str(j)

print(palindromic_product(3))