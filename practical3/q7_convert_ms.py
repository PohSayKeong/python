import math

n = int(input("please enter time in ms: "))

def convert_ms(n):
    second = math.floor(n/1000)
    second_final = second % 60
    minutes = second // 60
    minutes_final = minutes % 60
    hour = minutes // 60
    print(str(hour) + ":" + str(minutes_final) + ":" + str(second_final))

convert_ms(n)
