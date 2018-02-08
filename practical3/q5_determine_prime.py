import math

def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3,int(math.sqrt(n)) + 1,2):
        if n % i ==0:
            return False
    return True
    
numbers = []
for i in range(2,1000):
    if is_prime(i):
        numbers.append(str(i))

for i in range(0, len(numbers), 10):
    row = numbers[i:i+10]
    print(' '.join(row))
