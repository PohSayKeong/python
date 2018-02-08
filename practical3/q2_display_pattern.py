n = int(input("please input integer: "))
for i in range (n):
    line = ''
    for x in range (i+1):
        line = line + " " + str(x+1)
    print(line)
