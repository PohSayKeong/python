num = int(input("integer: "))
i = 2
factors = []

while num > i and i < 12:
    print(num)
    if num % i == 0:
        factors.append(i)
        num = num / i
        i = 2
    else:
        i += 1
factors.append(int(num))
print(factors)
