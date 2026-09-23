def sumInt(num):
    res = 0
    while num != 0:
        last = num % 10
        res += last
        num //= 10
    return res
print(sumInt(123321))