import math
radius = float(input("Please enter radius of cylinder:"))
length = float(input("Please enter length of cylinder:"))
area = radius * radius * math.pi
volume = area * length
print ("area: {0:.1f}".format(area))
print ("volume: {0:.1f}".format(volume))
