from math import log10
def reverse_int(num):
    if num < 10:
        return num
    else:
        ones = num % 10
        rest = num // 10
        return ones * 10 ** int(log10(rest) + 1) + reverse_int(rest)
print (reverse_int(12345))
