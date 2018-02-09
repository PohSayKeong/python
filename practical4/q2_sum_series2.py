n = int(input("please input your integer: "))

mi = 0

def sum_series2(i,mi):
    if i == 0:
        return mi
    else:
        mi += i/(i*2+1)
        return sum_series2(i-1,mi)

print(sum_series2(n,mi))
