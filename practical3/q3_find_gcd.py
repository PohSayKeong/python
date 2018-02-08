minimum2416 = min(24,16)
minimum25525 = min(255,25)
def gcd(minimum,n1,n2):
    if n1 % minimum == 0 and n2 % minimum == 0:
        return minimum
    else:
        return gcd(minimum-1,n1,n2)
print(gcd(minimum2416,24,16))
print(gcd(minimum25525,255,25))
    
