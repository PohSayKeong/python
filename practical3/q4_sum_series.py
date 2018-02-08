def m_series(i):
    mi = 0
    for x in range (i):
        mi += (x+1)/(x+2)
    res.append('\t%.4f' % mi)

val = ['i']
res = ['\tm(i)']
for i in range(20):
    val.append(str(i+1))
    m_series(i+1)
for row in zip(val,res):
    print(row)
    print (' '.join(row))
