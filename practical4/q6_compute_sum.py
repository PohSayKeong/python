def sum_digits(n):
    if len(str(n)) == 0:
        return 0
    return int(str(n)[0]) + sum_digits(str(n)[1:])

print (sum_digits(234))
