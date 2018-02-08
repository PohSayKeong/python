n = int(input("Please enter your integer: "))
def reverse_int(n):
    reverse = 0
    while(n > 0):
        remainder = n %10
        reverse = (reverse *10) + remainder
        n = n //10
    return reverse
print(reverse_int(n))
