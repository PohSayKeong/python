n1 = int(input("first integer: "))
n2 = int(input("second integer: "))
minimum = min(n1,n2)
def gcf(minimum,n1,n2):
    if n1 % minimum == 0 and n2 % minimum == 0:
        return minimum
    else:
        return gcf(minimum-1,n1,n2)
print(gcf(minimum,n1,n2))
