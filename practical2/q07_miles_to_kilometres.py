miles = [1,2,3,4,5,6,7,8,9,10]
kilometers = ["\tKilometers"]
kilometers_specific = [20,25,60,65]
miles_specific = ["\tMiles"]
for i in range (len(miles)):
    x = "\t" + str(round(miles[i] * 1.609,3))
    kilometers.append(x)
for i in range (len(miles)):
    miles[i] = str(miles[i])
miles.insert(0,"Miles")
for i in range (len(kilometers_specific)):
    x = "\t\t" + str(round(kilometers_specific[i] / 1.609,3))
    miles_specific.append(x)
for i in range (len(kilometers_specific)):
    kilometers_specific[i] = "\t   " + str(kilometers_specific[i])
kilometers_specific.insert(0,"Kilometres")
for row in zip(miles,kilometers,kilometers_specific,miles_specific):
    print (' '.join(row))
