n = int(input("please input your integer: "))

mi = 0

def sum_series1(i,mi):
    if i == 0:
        return mi
    else:
        mi += 1/i
        return sum_series1(i-1,mi)

print(sum_series1(n,mi))
