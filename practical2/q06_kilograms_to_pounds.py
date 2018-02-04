kilograms = [1,2,3,4,5,6,7,8,9,10]
pounds = ["\tPounds"]
for i in range (len(kilograms)):
    x = "\t\t" + str(round(kilograms[i] * 2.2,1))
    pounds.append(x)
for i in range (len(kilograms)):
    kilograms[i] = str(kilograms[i])
kilograms.insert(0,"Kilograms")
for row in zip(kilograms,pounds):
    print (' '.join(row))
